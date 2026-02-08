---
tags:
  - compute
---

# PySpark Decorators

## Performance Measurement & Debugging

This collection of decorators helps in measuring execution time, analyzing execution plans, and debugging PySpark DataFrames.

```python
import time
import logging
from pyspark.sql import DataFrame

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def measure_time(func):
    """Decorator to measure execution time of a function"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"Starting {func.__name__}")
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"Completed {func.__name__} in {duration:.2f} seconds")
        
        return result
    return wrapper

def show_execution_plan(func):
    """Decorator to show query execution plan"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if isinstance(result, DataFrame):
            logger.info(f"\nExecution plan for {func.__name__}:")
            result.explain()
        
        return result
    return wrapper

def cache_and_count(func):
    """Decorator to cache DataFrame and show count"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if isinstance(result, DataFrame):
            result.cache()
            count = result.count()
            logger.info(f"{func.__name__} returned {count} rows (cached)")
        
        return result
    return wrapper

def show_sample_output(n=5):
    """Decorator to show sample rows from resulting DataFrame"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if isinstance(result, DataFrame):
                logger.info(f"\nSample output from {func.__name__}:")
                result.show(n, truncate=False)
            
            return result
        return wrapper
    return decorator

def log_checkpoint(func):
    """Decorator to log DataFrame schema and statistics"""
    def wrapper(*args, **kwargs):
        logger.info(f"\n{'='*50}")
        logger.info(f"Checkpoint: {func.__name__}")
        logger.info(f"{'='*50}")
        
        result = func(*args, **kwargs)
        
        if isinstance(result, DataFrame):
            logger.info("\nSchema:")
            result.printSchema()
            
            logger.info(f"\nRow count: {result.count()}")
            logger.info(f"Partition count: {result.rdd.getNumPartitions()}")
        
        logger.info(f"{'='*50}\n")
        return result
    return wrapper

def log_partitions(func):
    """Decorator to log partition information"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if isinstance(result, DataFrame):
            num_partitions = result.rdd.getNumPartitions()
            logger.info(f"{func.__name__} - Number of partitions: {num_partitions}")
            
            partition_sizes = result.rdd.glom().map(len).collect()
            logger.info(f"Partition sizes: {partition_sizes}")
        
        return result
    return wrapper
```
