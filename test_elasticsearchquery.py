# test_elasticsearchquery.py
"""
Tests for ElasticsearchQuery module.
"""

import unittest
from elasticsearchquery import ElasticsearchQuery

class TestElasticsearchQuery(unittest.TestCase):
    """Test cases for ElasticsearchQuery class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ElasticsearchQuery()
        self.assertIsInstance(instance, ElasticsearchQuery)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ElasticsearchQuery()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
