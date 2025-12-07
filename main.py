import warnings
import logging
import sys
from config import LOG_LEVEL, LOG_FORMAT, LOG_FILE

warnings.filterwarnings("ignore", category=UserWarning, module="google.adk")

# Configure logging
def setup_logging():
    """Setup centralized logging configuration."""
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL),
        format=LOG_FORMAT,
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    logger = logging.getLogger('travel_agent.main')
    logger.info("Logging system initialized")
    return logger

def main():
    """Main function with options for demo or interactive mode."""
    logger = setup_logging()
    logger.info("Starting Travel Agent Application")
    
    try:
        print("Welcome to Travel Agent!!")
        logger.info("Application started successfully")
        
        # Example of using the logging system for business events
        from logging_utils import log_business_event
        log_business_event("application_started", {"version": "1.0", "mode": "demo"})
        
        # Add any additional main application logic here
        
    except Exception as e:
        logger.error(f"Error in main application: {str(e)}", exc_info=True)
        raise
    finally:
        logger.info("Travel Agent Application shutting down")

if __name__ == "__main__":
    main()
