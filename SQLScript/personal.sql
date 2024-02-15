-- Table: public.personal

-- DROP TABLE IF EXISTS public.personal;

CREATE TABLE IF NOT EXISTS public.personal
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    surname character varying(50) COLLATE pg_catalog."default" NOT NULL,
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    patronymic character varying(50) COLLATE pg_catalog."default",
    "postId" integer,
    CONSTRAINT personal_pkey PRIMARY KEY (id),
    CONSTRAINT "FK_post" FOREIGN KEY ("postId")
        REFERENCES public.post (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.personal
    OWNER to postgres;