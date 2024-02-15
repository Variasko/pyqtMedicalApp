-- Table: public.recipe

-- DROP TABLE IF EXISTS public.recipe;

CREATE TABLE IF NOT EXISTS public.recipe
(
    id integer NOT NULL,
    recipe character varying(10000) COLLATE pg_catalog."default",
    "personalId" integer,
    "patientId" integer,
    "diagnosisId" integer,
    CONSTRAINT recipe_pkey PRIMARY KEY (id),
    CONSTRAINT "FK_diagnosis" FOREIGN KEY ("diagnosisId")
        REFERENCES public.diagnosis (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "FK_patientId" FOREIGN KEY ("patientId")
        REFERENCES public.patient (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "FK_personal" FOREIGN KEY ("personalId")
        REFERENCES public.personal (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.recipe
    OWNER to postgres;