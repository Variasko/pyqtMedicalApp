-- Table: public.hospitalization

-- DROP TABLE IF EXISTS public.hospitalization;

CREATE TABLE IF NOT EXISTS public.hospitalization
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    "dateGospitalizated" date NOT NULL,
    "patientId" integer NOT NULL,
    "personalId" integer NOT NULL,
    "diagnosisId" integer NOT NULL,
    "hospitalizationGoal" character varying(250) COLLATE pg_catalog."default" NOT NULL,
    "departmentId" integer NOT NULL,
    "isBudget" bit(1) NOT NULL,
    "dischargeDate" date NOT NULL,
    "hospitalizationCode" integer NOT NULL,
    "hospitalizationRefusal" bit(1) NOT NULL,
    "hospitalizationCancel" bit(1) NOT NULL,
    "reasonForHospitalizationCancel" character varying(1000) COLLATE pg_catalog."default",
    CONSTRAINT gostopilization_pkey PRIMARY KEY (id),
    CONSTRAINT "FK_department" FOREIGN KEY ("departmentId")
        REFERENCES public.department (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "FK_diagnosis" FOREIGN KEY ("diagnosisId")
        REFERENCES public.diagnosis (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "FK_patient" FOREIGN KEY ("patientId")
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

ALTER TABLE IF EXISTS public.hospitalization
    OWNER to postgres;