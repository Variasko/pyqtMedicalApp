-- Table: public.RDMType

-- DROP TABLE IF EXISTS public."RDMType";

CREATE TABLE IF NOT EXISTS public."RDMType"
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "RDMType_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."RDMType"
    OWNER to postgres;