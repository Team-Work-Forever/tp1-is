CREATE TABLE public.imported_documents (
	id              serial PRIMARY KEY,
	file_name       VARCHAR(250) UNIQUE NOT NULL,
	xml             XML NOT NULL,
	created_on      TIMESTAMP NOT NULL DEFAULT NOW(),
	updated_on      TIMESTAMP NOT NULL DEFAULT NOW(),
	deleted_on      TIMESTAMP DEFAULT NULL 
);

CREATE VIEW active_imported_documents
AS
SELECT
*
FROM imported_documents
WHERE deleted_on IS NULL;