
CREATE TABLE public.menu
(
    idm integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 ),
    nome text,
    prezzo double precision,
    PRIMARY KEY (idm)
);

CREATE TABLE public.tavoli
(
    idt integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 ),
    n_posti integer,
    PRIMARY KEY (idt)
);

CREATE TABLE public.prenotazioni
(
    idp integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 ),
    data date,
    idme integer,
    idta integer,
    PRIMARY KEY (idp),
    CONSTRAINT id_menu FOREIGN KEY (idme)
        REFERENCES public.menu (idm) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT id_tavolo FOREIGN KEY (idta)
        REFERENCES public.tavoli (idt) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);



SELECT * FROM public.menu;
SELECT * FROM public.tavoli;
SELECT * FROM public.prenotazioni;



select menu.nome, prenotazioni.data, tavoli.n_posti 
from public.menu, public.prenotazioni, public.tavoli 
where menu.idm = prenotazioni.idme and tavoli.idt = prenotazioni.idta;

select menu.nome, prenotazioni.data, tavoli.n_posti 
from public.menu, public.prenotazioni, public.tavoli 
where prenotazioni.data >= '01/03/2014' and menu.idm = prenotazioni.idme and tavoli.idt = prenotazioni.idta;



INSERT INTO public.menu(
	nome, prezzo)
	VALUES ( 'Brodino di Pesce', 6.6);

INSERT INTO public.menu(
	nome, prezzo)
	VALUES ( 'Bruschette varie', 3.4);

INSERT INTO public.menu(
	nome, prezzo)
	VALUES ( 'Salumi e formaggio', 4);

INSERT INTO public.menu(
	nome, prezzo)
	VALUES ( 'Gallette e acqua', 1);


INSERT INTO public.tavoli(
	n_posti)
	VALUES ( 4);
INSERT INTO public.tavoli(
	n_posti)
	VALUES ( 2);
INSERT INTO public.tavoli(
	n_posti)
	VALUES ( 12);
INSERT INTO public.tavoli(
	n_posti)
	VALUES ( 1);
INSERT INTO public.tavoli(
	n_posti)
	VALUES ( 99);
INSERT INTO public.tavoli(
	n_posti)
	VALUES ( 7);
	
INSERT INTO public.prenotazioni(
	data, idta, idme)
	VALUES ( '23/07/2013', 3, 1);	
	
INSERT INTO public.prenotazioni(
	data, idta, idme)
	VALUES ( '24/07/2013', 2, 3);	

INSERT INTO public.prenotazioni(
	data, idta, idme)
	VALUES ( '24/07/2013', 1, 2);	
INSERT INTO public.prenotazioni(
	data, idta, idme)
	VALUES ( '24/07/2013', 1, 2);	

INSERT INTO public.prenotazioni(
	data, idta, idme)
	VALUES ( '07/06/2013', 4, 3);	
INSERT INTO public.prenotazioni(
	data, idta, idme)
	VALUES ( '11/08/2013', 5, 2);	
INSERT INTO public.prenotazioni(
	data, idta, idme)
	VALUES ( '06/08/2013', 4, 1);	
INSERT INTO public.prenotazioni(
	data, idta, idme)
	VALUES ( '09/08/2013', 6, 3);	
INSERT INTO public.prenotazioni(
	data, idta, idme)
	VALUES ( '14/07/2013', 5, 2);	
INSERT INTO public.prenotazioni(
	data, idta, idme)
	VALUES ( '13/09/2013', 5, 4);	
	
DELETE FROM public.prenotazioni
	WHERE prenotazioni.data == '07/06/2013';