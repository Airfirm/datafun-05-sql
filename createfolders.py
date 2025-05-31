import os
import pathlib
import pandas as pd
from utils_logger import logger

def create_sample_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Creates sample author and book data as DataFrames"""
    # Author data with UUIDs
    authors_data = {
        'author_id': [
            '10f88232-1ae7-4d88-a6a2-dfcebb22a596',
            'c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70',
            'e0b75863-866d-4db4-85c7-df9bb8ee6dab',
            '7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d',
            '8d8107b6-1f24-481c-8a21-7d72b13b59b5',
            '0cc3c8e4-e0c0-482f-b2f7-af87330de214',
            '4dca0632-2c53-490c-99d5-4f6d41e56c0e',
            '16f3e0a1-24cb-4ed6-a50d-509f63e367f7',
            '06cf58ab-90f1-448d-8e54-055e4393e75c',
            '6b693b96-394a-4a1d-a4e2-792a47d7a568'
        ],
        'first': ['Harper', 'George', 'F. Scott', 'Aldous', 'J.D.', 'Ray', 'Jane', 'J.R.R.', 'J.R.R.', 'J.K.'],
        'last': ['Lee', 'Orwell', 'Fitzgerald', 'Huxley', 'Salinger', 'Bradbury', 'Austen', 'Tolkien', 'Tolkien', 'Rowling']
    }

    # Book data with UUIDs and author relationships
    books_data = {
        'book_id': [
            'd6f83870-ff21-4a5d-90ab-26a49ab6ed12',
            '0f5f44f7-44d8-4f49-b8c4-c64d847587d3',
            'f9d9e7de-c44d-4d1d-b3ab-59343bf32bc2',
            '38e530f1-228f-4d6e-a587-2ed4d6c44e9c',
            'c2a62a4b-cf5c-4246-9bf7-b2601d542e6d',
            '3a1d835c-1e15-4a48-8e8c-b12239604e98',
            'c6e67918-e509-4a6b-bc3a-979f6ad802f0',
            'be951205-6cc2-4b3d-96f1-7257b8fc8c0f',
            'dce0f8f2-d3ed-48a9-b8ff-960b6baf1f6f',
            'ca8e64c3-1e67-47f5-82cc-3e4e30f63b75'
        ],
        'title': [
            'To Kill a Mockingbird',
            '1984',
            'The Great Gatsby',
            'Brave New World',
            'The Catcher in the Rye',
            'Fahrenheit 451',
            'Pride and Prejudice',
            'The Hobbit',
            'The Lord of the Rings',
            'Harry Potter and the Philosopher\'s Stone'
        ],
        'year_published': [1960, 1949, 1925, 1932, 1951, 1953, 1813, 1937, 1954, 1997],
        'author_id': [
            '10f88232-1ae7-4d88-a6a2-dfcebb22a596',
            'c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70',
            'e0b75863-866d-4db4-85c7-df9bb8ee6dab',
            '7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d',
            '8d8107b6-1f24-481c-8a21-7d72b13b59b5',
            '0cc3c8e4-e0c0-482f-b2f7-af87330de214',
            '4dca0632-2c53-490c-99d5-4f6d41e56c0e',
            '16f3e0a1-24cb-4ed6-a50d-509f63e367f7',
            '06cf58ab-90f1-448d-8e54-055e4393e75c',
            '6b693b96-394a-4a1d-a4e2-792a47d7a568'
        ]
    }
    
    return pd.DataFrame(authors_data), pd.DataFrame(books_data)

def export_to_csv(df: pd.DataFrame, folder: pathlib.Path, filename: str) -> None:
    """Exports a DataFrame to CSV in the specified folder"""
    try:
        filepath = folder.joinpath(filename)
        df.to_csv(filepath, index=False)
        logger.info(f"Created {filepath}")
    except Exception as e:
        logger.error(f"Failed to create {filename}: {e}")
        raise

def main() -> None:
    logger.info("Starting data export...")
    
    # Define paths
    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    PROJECT_DATA_FOLDER = ROOT_DIR.joinpath("project_data")
    
    # Create project folder
    PROJECT_DATA_FOLDER.mkdir(exist_ok=True)
    logger.info(f"Created project folder: {PROJECT_DATA_FOLDER}")

    # Create sample data
    authors_df, books_df = create_sample_data()
    
    # Export to CSV
    export_to_csv(authors_df, PROJECT_DATA_FOLDER, "authors.csv")
    export_to_csv(books_df, PROJECT_DATA_FOLDER, "books.csv")
    
    logger.info("Data export completed successfully")

if __name__ == '__main__':
    main()