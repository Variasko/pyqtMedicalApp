-- Table: public.gender

-- DROP TABLE IF EXISTS public.gender;

CREATE TABLE IF NOT EXISTS public.gender
(
    "id " integer NOT NULL,
    gender character varying(7) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT gender_pkey PRIMARY KEY ("id ")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.gender
    OWNER to postgres;