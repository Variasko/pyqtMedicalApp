-- Table: public.patient

-- DROP TABLE IF EXISTS public.patient;

CREATE TABLE IF NOT EXISTS public.patient
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    surname character varying(50) COLLATE pg_catalog."default" NOT NULL,
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    patronymic character varying(50) COLLATE pg_catalog."default",
    "pasportSerial" integer NOT NULL,
    "pasportNumber" integer NOT NULL,
    birthday date,
    "genderId" integer,
    address character varying(100) COLLATE pg_catalog."default",
    "contactPhoneNumber" character varying(12) COLLATE pg_catalog."default" NOT NULL,
    email character varying(50) COLLATE pg_catalog."default",
    "numberMedicalCard" integer,
    "dateGetMedicalCard" date,
    "dateLastVisit" date,
    "dateNextVisit" date,
    "numberInsurancePolicy" integer NOT NULL,
    "dateOfDeadIncurancePolicy" date NOT NULL,
    "workingPlace" character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "InsuranceCompany" character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT patient_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.patient
    OWNER to postgres;