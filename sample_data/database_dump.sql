--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: adset_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.adset_group (
    adset_id integer,
    group_id integer
);


ALTER TABLE public.adset_group OWNER TO postgres;

--
-- Name: adsets; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.adsets (
    id integer NOT NULL,
    name character varying,
    optimization_goal character varying,
    campaign_id integer
);


ALTER TABLE public.adsets OWNER TO postgres;

--
-- Name: adsets_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.adsets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.adsets_id_seq OWNER TO postgres;

--
-- Name: adsets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.adsets_id_seq OWNED BY public.adsets.id;


--
-- Name: campaigns; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.campaigns (
    id integer NOT NULL,
    name character varying,
    objective character varying
);


ALTER TABLE public.campaigns OWNER TO postgres;

--
-- Name: campaigns_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.campaigns_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.campaigns_id_seq OWNER TO postgres;

--
-- Name: campaigns_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.campaigns_id_seq OWNED BY public.campaigns.id;


--
-- Name: groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.groups (
    id integer NOT NULL,
    name character varying
);


ALTER TABLE public.groups OWNER TO postgres;

--
-- Name: groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.groups_id_seq OWNER TO postgres;

--
-- Name: groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.groups_id_seq OWNED BY public.groups.id;


--
-- Name: adsets id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.adsets ALTER COLUMN id SET DEFAULT nextval('public.adsets_id_seq'::regclass);


--
-- Name: campaigns id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.campaigns ALTER COLUMN id SET DEFAULT nextval('public.campaigns_id_seq'::regclass);


--
-- Name: groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.groups ALTER COLUMN id SET DEFAULT nextval('public.groups_id_seq'::regclass);


--
-- Data for Name: adset_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.adset_group (adset_id, group_id) FROM stdin;
10	9
10	11
11	10
11	12
12	11
12	13
13	12
13	14
14	13
14	15
15	14
15	16
16	15
16	17
17	16
17	18
18	17
18	19
19	18
19	20
20	19
20	1
21	2
21	3
22	4
22	5
23	6
23	7
24	8
24	9
25	10
25	11
26	12
26	13
27	14
27	15
28	16
28	17
29	18
29	19
30	20
30	1
31	2
31	3
32	4
32	5
33	6
33	7
34	8
34	9
35	10
35	11
36	12
36	13
37	14
37	15
38	16
38	17
39	18
39	19
40	20
40	1
42	1
43	1
43	2
44	1
44	2
45	1
45	2
46	30
46	31
47	32
47	33
48	34
48	35
49	36
49	37
50	38
50	39
51	40
51	41
52	42
52	43
53	44
53	45
54	46
54	47
55	48
55	49
62	50
62	51
69	52
69	53
76	54
76	55
83	56
83	57
90	58
90	59
97	60
97	61
102	1
102	2
\.


--
-- Data for Name: adsets; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.adsets (id, name, optimization_goal, campaign_id) FROM stdin;
2	Adset 2	reach	1
3	Adset 3	clicks	2
4	Adset 4	engagement	2
5	Adset 5	app_installs	3
6	Adset 6	leads	3
7	Adset 7	video_views	4
8	Adset 8	store_visits	4
9	Adset 9	messages	5
10	Adset 10	brand_awareness	5
11	Adset 11	catalog_sales	6
12	Adset 12	event_responses	6
13	Adset 13	catalog_sales	7
14	Adset 14	conversions	7
15	Adset 15	post_engagement	8
16	Adset 16	page_likes	8
17	Adset 17	offer_claims	9
18	Adset 18	video_views	9
19	Adset 19	app_engagement	10
20	Adset 20	impressions	10
21	Adset 21	reach	11
22	Adset 22	clicks	11
23	Adset 23	engagement	12
24	Adset 24	app_installs	12
25	Adset 25	leads	13
26	Adset 26	video_views	13
27	Adset 27	store_visits	14
28	Adset 28	messages	14
29	Adset 29	brand_awareness	15
30	Adset 30	catalog_sales	15
31	Adset 31	event_responses	16
32	Adset 32	catalog_sales	16
33	Adset 33	conversions	17
34	Adset 34	post_engagement	17
35	Adset 35	page_likes	18
36	Adset 36	offer_claims	18
37	Adset 37	video_views	19
38	Adset 38	app_engagement	19
39	Adset 39	impressions	20
40	Adset 40	reach	20
42	a	b	1
43	Test Adset	Reach	1
44	Test Adset	Reach	1
45	Test Adset	Reach	1
46	Test Adset	Reach	38
47	Test Adset	Reach	39
48	Test Adset	Reach	40
49	Test Adset	Reach	41
50	Test Adset	Reach	42
51	Test Adset	Reach	43
52	Test Adset	Reach	44
53	Test Adset	Reach	45
54	Test Adset	Reach	46
55	Test Adset	Reach	47
56	Adset 1	Reach	\N
57	Adset 2	Link Clicks	\N
58	Adset 1	Reach	\N
59	Adset 1	Reach	\N
60	Adset 1	Reach	\N
62	Test Adset	Reach	48
63	Adset 1	Reach	\N
64	Adset 2	Link Clicks	\N
65	Adset 1	Reach	\N
66	Adset 1	Reach	\N
67	Adset 1	Reach	\N
69	Test Adset	Reach	49
70	Adset 1	Reach	\N
71	Adset 2	Link Clicks	\N
72	Adset 1	Reach	\N
73	Adset 1	Reach	\N
74	Adset 1	Reach	\N
76	Test Adset	Reach	50
77	Adset 1	Reach	\N
78	Adset 2	Link Clicks	\N
79	Adset 1	Reach	\N
80	Adset 1	Reach	\N
81	Adset 1	Reach	\N
83	Test Adset	Reach	51
84	Adset 1	Reach	\N
85	Adset 2	Link Clicks	\N
86	Adset 1	Reach	\N
87	Updated Adset	Reach	\N
88	Adset 1	Reach	\N
90	Test Adset	Reach	52
91	Adset 1	Reach	\N
92	Adset 2	Link Clicks	\N
93	Adset 1	Reach	\N
94	Updated Adset	Reach	\N
95	Adset 1	Reach	\N
97	Test Adset	Reach	53
98	Adset 1	Reach	\N
99	Adset 2	Link Clicks	\N
100	Adset 1	Reach	\N
101	Updated Adset	Reach	\N
102	New Name	New Goal	1
\.


--
-- Data for Name: campaigns; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.campaigns (id, name, objective) FROM stdin;
1	Campaign 1	Awareness
2	Campaign 2	Traffic
3	Campaign 3	Conversion
4	Campaign 4	Engagement
5	Campaign 5	Reach
6	Campaign 6	App Installs
7	Campaign 7	Lead Generation
8	Campaign 8	Video Views
9	Campaign 9	Store Visits
10	Campaign 10	Messages
11	Campaign 11	Brand Awareness
12	Campaign 12	Product Catalog Sales
13	Campaign 13	Event Responses
14	Campaign 14	Catalog Sales
15	Campaign 15	Conversions
16	Campaign 16	Post Engagement
17	Campaign 17	Page Likes
18	Campaign 18	Offer Claims
19	Campaign 19	Video Views
20	Campaign 20	App Engagement
22	Campaign 1	Awareness
23	Campaign 2	Traffic
24	Campaign 1	Awareness
25	Campaign 2	Traffic
26	Campaign 1	Awareness
27	Campaign 2	Traffic
28	Campaign 1	Awareness
29	Campaign 2	Traffic
30	Campaign 1	Awareness
31	Campaign 2	Traffic
32	Campaign 1	Awareness
33	Campaign 2	Traffic
34	\N	\N
35	\N	\N
36	\N	\N
37	\N	\N
38	\N	\N
39	\N	\N
40	\N	\N
41	\N	\N
42	\N	\N
43	\N	\N
44	\N	\N
45	\N	\N
46	\N	\N
47	\N	\N
48	\N	\N
49	\N	\N
50	\N	\N
51	\N	\N
52	\N	\N
53	\N	\N
\.


--
-- Data for Name: groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.groups (id, name) FROM stdin;
1	Group 1
2	Group 2
3	Group 3
4	Group 4
5	Group 5
6	Group 6
7	Group 7
8	Group 8
9	Group 9
10	Group 10
11	Group 11
12	Group 12
13	Group 13
14	Group 14
15	Group 15
16	Group 16
17	Group 17
18	Group 18
19	Group 19
20	Group 20
21	Group003
22	\N
23	\N
24	\N
25	\N
26	\N
27	\N
28	\N
29	\N
30	\N
31	\N
32	\N
33	\N
34	\N
35	\N
36	\N
37	\N
38	\N
39	\N
40	\N
41	\N
42	\N
43	\N
44	\N
45	\N
46	\N
47	\N
48	\N
49	\N
50	\N
51	\N
52	\N
53	\N
54	\N
55	\N
56	\N
57	\N
58	\N
59	\N
60	\N
61	\N
62	Test Group
63	Group 1
64	Group 2
65	Test Group
66	Updated Group
67	New Name
69	Test Group
70	Group 1
71	Group 2
72	Test Group
73	Updated Group
74	New Name
\.


--
-- Name: adsets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.adsets_id_seq', 103, true);


--
-- Name: campaigns_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.campaigns_id_seq', 53, true);


--
-- Name: groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.groups_id_seq', 75, true);


--
-- Name: adsets adsets_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.adsets
    ADD CONSTRAINT adsets_pkey PRIMARY KEY (id);


--
-- Name: campaigns campaigns_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.campaigns
    ADD CONSTRAINT campaigns_pkey PRIMARY KEY (id);


--
-- Name: groups groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (id);


--
-- Name: ix_adsets_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_adsets_id ON public.adsets USING btree (id);


--
-- Name: ix_adsets_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_adsets_name ON public.adsets USING btree (name);


--
-- Name: ix_campaigns_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_campaigns_id ON public.campaigns USING btree (id);


--
-- Name: ix_campaigns_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_campaigns_name ON public.campaigns USING btree (name);


--
-- Name: ix_groups_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_groups_id ON public.groups USING btree (id);


--
-- Name: ix_groups_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_groups_name ON public.groups USING btree (name);


--
-- Name: adset_group adset_group_adset_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.adset_group
    ADD CONSTRAINT adset_group_adset_id_fkey FOREIGN KEY (adset_id) REFERENCES public.adsets(id);


--
-- Name: adset_group adset_group_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.adset_group
    ADD CONSTRAINT adset_group_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.groups(id);


--
-- Name: adsets adsets_campaign_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.adsets
    ADD CONSTRAINT adsets_campaign_id_fkey FOREIGN KEY (campaign_id) REFERENCES public.campaigns(id);


--
-- PostgreSQL database dump complete
--

