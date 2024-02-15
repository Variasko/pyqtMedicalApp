-- Table: public.theRapeuticAndDiagnosticMeasures

-- DROP TABLE IF EXISTS public."theRapeuticAndDiagnosticMeasures";

CREATE TABLE IF NOT EXISTS public."theRapeuticAndDiagnosticMeasures"
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    "patientId" integer NOT NULL,
    "dateImplement" date,
    "personalId" integer NOT NULL,
    "typeId" integer NOT NULL,
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    result character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    recommeds character varying(10000) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "theRapeuticAndDiagnosticMeasures_pkey" PRIMARY KEY (id),
    CONSTRAINT "FK_patient" FOREIGN KEY ("patientId")
        REFERENCES public.patient (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "FK_personal" FOREIGN KEY ("personalId")
        REFERENCES public.personal (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "FK_type" FOREIGN KEY ("typeId")
        REFERENCES public."RDMType" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."theRapeuticAndDiagnosticMeasures"
    OWNER to postgres;