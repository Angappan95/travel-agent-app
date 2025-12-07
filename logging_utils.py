"""
Logging utilities for the travel agent application.
Provides consistent logging patterns and helper functions.
"""

import logging
import functools
import time
from typing import Callable, Any, Optional, Dict

def log_function_call(func: Callable) -> Callable:
    """
    Decorator to automatically log function calls with execution time.
    
    Args:
        func: The function to wrap with logging
        
    Returns:
        Wrapped function with logging
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        logger = logging.getLogger(f'travel_agent.{func.__module__}.{func.__name__}')
        
        # Log function start
        func_args = ', '.join([str(arg) for arg in args[:2]])  # Log first 2 args only
        func_kwargs = ', '.join([f"{k}={v}" for k, v in list(kwargs.items())[:3]])  # Log first 3 kwargs
        
        logger.info(f"Function called: {func.__name__}({func_args}{', ' if func_kwargs else ''}{func_kwargs})")
        
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            
            # Log successful completion
            result_status = "unknown"
            if isinstance(result, dict) and "status" in result:
                result_status = result["status"]
            
            logger.info(f"Function completed: {func.__name__} - Status: {result_status} - Time: {execution_time:.3f}s")
            
            return result
            
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"Function failed: {func.__name__} - Error: {str(e)} - Time: {execution_time:.3f}s", exc_info=True)
            raise
    
    return wrapper

def log_agent_interaction(agent_name: str, action: str, details: str = ""):
    """
    Log agent interactions for flow tracking.
    
    Args:
        agent_name: Name of the agent
        action: Action being performed
        details: Additional details about the action
    """
    logger = logging.getLogger(f'travel_agent.agent_flow')
    logger.info(f"AGENT: {agent_name} | ACTION: {action} | DETAILS: {details}")

def log_search_metrics(search_type: str, query: str, results_count: int, filters: Optional[Dict] = None):
    """
    Log search metrics for performance tracking.
    
    Args:
        search_type: Type of search (flights, hotels, activities)
        query: Search query or destination
        results_count: Number of results found
        filters: Applied filters
    """
    logger = logging.getLogger(f'travel_agent.search_metrics')
    
    filters_str = ", ".join([f"{k}={v}" for k, v in (filters or {}).items()])
    logger.info(f"SEARCH: {search_type} | QUERY: {query} | RESULTS: {results_count} | FILTERS: {filters_str}")

def log_business_event(event_type: str, event_data: dict):
    """
    Log business events for analytics.
    
    Args:
        event_type: Type of business event
        event_data: Event data dictionary
    """
    logger = logging.getLogger(f'travel_agent.business_events')
    
    data_str = ", ".join([f"{k}={v}" for k, v in event_data.items()])
    logger.info(f"BUSINESS_EVENT: {event_type} | DATA: {data_str}")

class LoggingContext:
    """
    Context manager for grouped logging operations.
    """
    
    def __init__(self, operation_name: str, logger_name: str = 'travel_agent.operations'):
        self.operation_name = operation_name
        self.logger = logging.getLogger(logger_name)
        self.start_time: Optional[float] = None
    
    def __enter__(self):
        self.start_time = time.time()
        self.logger.info(f"Starting operation: {self.operation_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        execution_time = time.time() - (self.start_time or 0)
        
        if exc_type is None:
            self.logger.info(f"Operation completed: {self.operation_name} - Time: {execution_time:.3f}s")
        else:
            self.logger.error(f"Operation failed: {self.operation_name} - Error: {str(exc_val)} - Time: {execution_time:.3f}s")
        
        return False  # Don't suppress exceptions
    
    def log_step(self, step_name: str, details: str = ""):
        """Log a step within the operation."""
        self.logger.info(f"  Step: {step_name} | {details}")

# Example usage patterns for consistent logging
def log_travel_plan_start(source: str, destination: str, travelers: int, budget: Optional[int] = None):
    """Log the start of travel plan creation."""
    log_business_event("travel_plan_requested", {
        "source": source,
        "destination": destination,
        "travelers": travelers,
        "budget": budget or "unspecified"
    })

def log_travel_plan_completion(plan_data: dict):
    """Log the completion of travel plan creation."""
    total_cost = plan_data.get("cost_estimate", {}).get("total", "unknown")
    
    log_business_event("travel_plan_completed", {
        "destination": plan_data.get("trip_overview", {}).get("destination", "unknown"),
        "total_cost": total_cost,
        "duration": plan_data.get("trip_overview", {}).get("duration_days", "unknown")
    })