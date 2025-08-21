import unittest
from unittest.mock import AsyncMock, MagicMock
from gemini_webapi import GeminiClient, StreamChunk, StreamDelta


class TestStreamingFunctionality(unittest.TestCase):
    """Test cases for the streaming functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = GeminiClient.__new__(GeminiClient)
        
    def test_stream_types_creation(self):
        """Test that streaming types can be created properly."""
        # Test StreamDelta
        delta = StreamDelta(text="Hello")
        self.assertEqual(delta.text, "Hello")
        
        # Test StreamChunk
        chunk = StreamChunk(
            rcid="test_rcid",
            delta=delta,
            finish_reason=None
        )
        self.assertEqual(chunk.rcid, "test_rcid")
        self.assertEqual(chunk.delta.text, "Hello")
        self.assertIsNone(chunk.finish_reason)
        
    def test_stream_types_serialization(self):
        """Test that streaming types can be serialized properly."""
        delta = StreamDelta(text="Hello world")
        chunk = StreamChunk(rcid="test", delta=delta, finish_reason="stop")
        
        # Test that they can be converted to dict
        delta_dict = delta.model_dump()
        chunk_dict = chunk.model_dump()
        
        self.assertEqual(delta_dict["text"], "Hello world")
        self.assertEqual(chunk_dict["rcid"], "test")
        self.assertEqual(chunk_dict["finish_reason"], "stop")
        
    def test_methods_exist(self):
        """Test that the streaming methods exist in the client."""
        self.assertTrue(hasattr(GeminiClient, 'generate_content_stream'))
        
        # Check method is callable
        method = getattr(GeminiClient, 'generate_content_stream')
        self.assertTrue(callable(method))
        
    def test_streaming_method_signature(self):
        """Test that the streaming method has the expected signature."""
        import inspect
        sig = inspect.signature(GeminiClient.generate_content_stream)
        
        # Check required parameters
        self.assertIn('prompt', sig.parameters)
        self.assertIn('files', sig.parameters)
        self.assertIn('model', sig.parameters)
        self.assertIn('gem', sig.parameters)
        self.assertIn('chat', sig.parameters)


if __name__ == '__main__':
    unittest.main()