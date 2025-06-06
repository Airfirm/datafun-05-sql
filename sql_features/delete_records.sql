-- Delete author only if they have this specific book
DELETE FROM authors
--WHERE author_id = 'AUTHOR_016'
WHERE author_id = 'AUTHOR_011'
AND EXISTS (
    SELECT 1 FROM books 
    WHERE books.author_id = authors.author_id
    --AND book_id = 'BOOK_027';
    AND book_id = 'BOOK_020'
);

-- Then delete the book
DELETE FROM books 
--WHERE book_id = 'BOOK_027';
WHERE book_id = 'BOOK_020';


--DELETE authors, books
--FROM authors
--INNER JOIN books ON authors.author_id = books.author_id
--WHERE authors.author_id = 'AUTHOR_16'
--AND books.book_id = 'BOOK_27';