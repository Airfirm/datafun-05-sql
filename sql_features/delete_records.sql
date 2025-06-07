-- Delete author only if they have this specific book
DELETE FROM authors
WHERE author_id = 'AUTHOR_016'
AND EXISTS (
    SELECT 1 FROM books 
    WHERE books.author_id = authors.author_id
    AND book_id = 'BOOK_027'
);

-- Then delete the book
DELETE FROM books 
WHERE book_id = 'BOOK_027';

