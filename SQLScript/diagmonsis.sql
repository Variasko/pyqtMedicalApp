-- Table: public.diagnosis

-- DROP TABLE IF EXISTS public.diagnosis;

CREATE TABLE IF NOT EXISTS public.diagnosis
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    recommends character varying(10000) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT diagnosys_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.diagnosis
    OWNER to postgres;