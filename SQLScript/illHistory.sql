-- Table: public.illHistory

-- DROP TABLE IF EXISTS public."illHistory";

CREATE TABLE IF NOT EXISTS public."illHistory"
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    "patientId" integer NOT NULL,
    "diagnosisId" integer NOT NULL,
    "illnessDate" date,
    "recoverydDate" date,
    CONSTRAINT "illHistory_pkey" PRIMARY KEY (id),
    CONSTRAINT "FK_diagnosis" FOREIGN KEY ("diagnosisId")
        REFERENCES public.diagnosis (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "FK_patient" FOREIGN KEY ("patientId")
        REFERENCES public.patient (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."illHistory"
    OWNER to postgres;