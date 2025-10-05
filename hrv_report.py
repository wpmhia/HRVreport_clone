#!/usr/bin/env python3
"""
HRV Report Generator
A simple module for generating Heart Rate Variability reports with debugging support.
"""

import logging
import sys
from typing import List, Dict, Any


# Configure logging for debugging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class HRVAnalyzer:
    """Analyzes heart rate variability data."""
    
    def __init__(self, debug: bool = False):
        """Initialize the HRV analyzer.
        
        Args:
            debug: Enable debug mode for verbose logging
        """
        self.debug = debug
        if debug:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
        
        logger.debug("HRVAnalyzer initialized with debug=%s", debug)
    
    def calculate_rmssd(self, rr_intervals: List[float]) -> float:
        """Calculate Root Mean Square of Successive Differences (RMSSD).
        
        Args:
            rr_intervals: List of RR intervals in milliseconds
            
        Returns:
            RMSSD value
        """
        logger.debug("Calculating RMSSD for %d intervals", len(rr_intervals))
        
        if len(rr_intervals) < 2:
            logger.warning("Not enough intervals to calculate RMSSD")
            return 0.0
        
        # Calculate successive differences
        successive_diffs = [abs(rr_intervals[i+1] - rr_intervals[i]) 
                           for i in range(len(rr_intervals) - 1)]
        
        logger.debug("Successive differences calculated: %s", successive_diffs[:5])
        
        # Calculate mean of squared differences
        squared_diffs = [diff ** 2 for diff in successive_diffs]
        mean_squared_diff = sum(squared_diffs) / len(squared_diffs)
        
        # Calculate root
        rmssd = mean_squared_diff ** 0.5
        
        logger.debug("RMSSD calculated: %.2f ms", rmssd)
        return rmssd
    
    def calculate_sdnn(self, rr_intervals: List[float]) -> float:
        """Calculate Standard Deviation of NN intervals (SDNN).
        
        Args:
            rr_intervals: List of RR intervals in milliseconds
            
        Returns:
            SDNN value
        """
        logger.debug("Calculating SDNN for %d intervals", len(rr_intervals))
        
        if len(rr_intervals) < 2:
            logger.warning("Not enough intervals to calculate SDNN")
            return 0.0
        
        mean = sum(rr_intervals) / len(rr_intervals)
        logger.debug("Mean RR interval: %.2f ms", mean)
        
        variance = sum((x - mean) ** 2 for x in rr_intervals) / len(rr_intervals)
        sdnn = variance ** 0.5
        
        logger.debug("SDNN calculated: %.2f ms", sdnn)
        return sdnn
    
    def generate_report(self, rr_intervals: List[float]) -> Dict[str, Any]:
        """Generate a complete HRV report.
        
        Args:
            rr_intervals: List of RR intervals in milliseconds
            
        Returns:
            Dictionary containing HRV metrics
        """
        logger.info("Generating HRV report for %d intervals", len(rr_intervals))
        
        report = {
            'num_intervals': len(rr_intervals),
            'mean_rr': sum(rr_intervals) / len(rr_intervals) if rr_intervals else 0,
            'rmssd': self.calculate_rmssd(rr_intervals),
            'sdnn': self.calculate_sdnn(rr_intervals)
        }
        
        logger.info("Report generated: %s", report)
        return report


def main():
    """Main function demonstrating HRV analysis with debugging."""
    logger.info("Starting HRV Report Generator")
    
    # Example RR intervals (in milliseconds)
    sample_data = [800, 810, 790, 805, 795, 808, 812, 798, 802, 807]
    
    logger.info("Processing sample data with %d intervals", len(sample_data))
    
    # Create analyzer with debug mode enabled
    analyzer = HRVAnalyzer(debug=True)
    
    # Generate report
    report = analyzer.generate_report(sample_data)
    
    # Display results
    print("\n" + "="*50)
    print("HRV REPORT")
    print("="*50)
    print(f"Number of intervals: {report['num_intervals']}")
    print(f"Mean RR interval: {report['mean_rr']:.2f} ms")
    print(f"RMSSD: {report['rmssd']:.2f} ms")
    print(f"SDNN: {report['sdnn']:.2f} ms")
    print("="*50 + "\n")
    
    logger.info("HRV Report Generator completed successfully")


if __name__ == "__main__":
    main()
