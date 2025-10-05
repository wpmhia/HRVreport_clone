#!/usr/bin/env python3
"""
Unit tests for HRV Report Generator
"""

import unittest
import logging
from hrv_report import HRVAnalyzer


class TestHRVAnalyzer(unittest.TestCase):
    """Test cases for HRVAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = HRVAnalyzer(debug=True)
        self.sample_data = [800, 810, 790, 805, 795, 808, 812, 798, 802, 807]
    
    def test_rmssd_calculation(self):
        """Test RMSSD calculation."""
        rmssd = self.analyzer.calculate_rmssd(self.sample_data)
        self.assertGreater(rmssd, 0)
        self.assertAlmostEqual(rmssd, 11.77, places=2)
    
    def test_sdnn_calculation(self):
        """Test SDNN calculation."""
        sdnn = self.analyzer.calculate_sdnn(self.sample_data)
        self.assertGreater(sdnn, 0)
        self.assertAlmostEqual(sdnn, 6.65, places=2)
    
    def test_empty_data(self):
        """Test handling of empty data."""
        rmssd = self.analyzer.calculate_rmssd([])
        sdnn = self.analyzer.calculate_sdnn([])
        self.assertEqual(rmssd, 0.0)
        self.assertEqual(sdnn, 0.0)
    
    def test_single_interval(self):
        """Test handling of single interval."""
        rmssd = self.analyzer.calculate_rmssd([800])
        sdnn = self.analyzer.calculate_sdnn([800])
        self.assertEqual(rmssd, 0.0)
        self.assertEqual(sdnn, 0.0)
    
    def test_report_generation(self):
        """Test full report generation."""
        report = self.analyzer.generate_report(self.sample_data)
        
        self.assertEqual(report['num_intervals'], 10)
        self.assertGreater(report['mean_rr'], 0)
        self.assertGreater(report['rmssd'], 0)
        self.assertGreater(report['sdnn'], 0)
    
    def test_debug_mode(self):
        """Test debug mode initialization."""
        debug_analyzer = HRVAnalyzer(debug=True)
        self.assertTrue(debug_analyzer.debug)
        
        normal_analyzer = HRVAnalyzer(debug=False)
        self.assertFalse(normal_analyzer.debug)


if __name__ == '__main__':
    # Suppress debug logs during testing for cleaner output
    logging.getLogger('__main__').setLevel(logging.CRITICAL)
    
    unittest.main(verbosity=2)
