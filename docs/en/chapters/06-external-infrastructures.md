# Chapter 6: External infrastructures

In this chapter, a Cloud Service Provider is called a CSP and a Wide Area Network Service Provider is called an NSP.

**External infrastructures cover:**

- External hosting (the Data Centre does not belong to the evaluated company).
- Cloud.
- Wide Area Network (WAN).

## Open questions

- How do you assure the environmental reporting requested from your CSP, as a client? What data points are reported? If you are a CSP, how do you provide this reporting?
- How does the CSP provide LCA input data? Which kind of input data?
- What is the CSP’s renewable energy policy? What is the transparency and traceability level of its GHG reporting in respect of its renewable energy purchases?
- How are Sovereignty and Resiliency considered in the cloud hosting policy?
- How is Sustainable IT integrated to the design and management of the CSP’s data centres, infrastructures and facilities?
- How is Sustainable IT integrated into the design and management of the CSP’s internal network (LAN) infrastructures and facilities?
- How is sustainable IT integrated to the selection and management of data centres’ physical assets (servers)?
- How do you assure the environmental reporting requested from your NSP, as a client? What data points are reported? How do you provide this reporting, if you are a NSP?
- How does the NSP provide LCA input data?
- What is the NSP’s renewable energy policy? What is the transparency and traceability level on its GHG reporting in respect of renewable energy purchase?
- What actions are taken to reduce the footprint of WAN equipment?

## 6.1 How do you assure the environmental reporting requested from your CSP, as a client? What data points are reported? If you are a CSP, how do you provide this reporting? {#q6-1}

### Rationale

Many digital policies encourage to “move to cloud” for different technical and financial reasons. However, the environmental footprint of many cloud providers, especially hyperscalers, remains very nebulous. As part of the scope 3 of their clients, the reporting coming from cloud providers must be transparent, covering the scope 3 (especially upstream) as well as the scopes 1 and 2. Reported data must help the clients to measure the footprint of the services they use.

### Evaluation criteria

| Evaluation criterion | Recommended priority | Proposed weighting (total = 10 points) |
|---|---|---|
| Emissions under all scopes (1, 2, 3 of the GHG Protocol) are requested from the cloud providers (or provided by the organisation, if it is a CSP). | P1 | 3 |
| The reporting requested (or provided) must include not only GHG emissions (including fugitive emissions of coolant, for example), but also other environmental impacts:<br>• Water consumption and WUE indicator.<br>• CO₂ equivalent emissions and CUE indicator.<br>• Depletion of mineral abiotic resources.<br>• Primary Energy consumption.<br>• Land use.<br>• And other relevant impacts necessary to evaluate impacts on biodiversity, in line with CSRD: acidification of soils and water, eutrophication, etc. | P1 | 3 |
| The evaluation of the environmental footprint of the organisation takes into account all the different types of cloud services that it uses or provides: IaaS, PaaS, SaaS, CaaS, etc. | P2 | 2 |
| The CSP is asked to respect the EU Code of Conduct for Data Centres, with proven engagement (signature on the charter). | P2 | 2 |

## 6.2 How does the CSP provide LCA input data? Which kind of input data? {#q6-2}

### Rationale

Reported data must help the clients to measure the footprint of the services they use. As seen before, systemic methodologies, such as LCA, must be used in order to get an objective evaluation and prevent pollution transfers (in the different phases of the life cycle and on different environmental impacts). This use is possible only if input data such as lifespan and types of servers, number of duplications of data, technical architectures, are provided. Otherwise, incertitude level is too high, and these methodologies cannot be used to help with decision making.

### Evaluation criteria

| Evaluation criterion | Recommended priority | Proposed weighting (total = 10 points) |
|---|---|---|
| Input data for a Life Cycle Assessment of any digital service that uses cloud must be requested of the CSP (or provided by the CSP). For example:<br>• How many times the data is duplicated (as a function of the SLA level, if needed).<br>• Average lifetime of servers and other IT equipment.<br>• Inventory of infrastructures used by data centres (chillers, electrical converters, diesel generators, stored fuel, etc.).<br>• Lifetime of the data centres and their infrastructures.<br>• Annual consumptions of energy, water, and coolant are provided.<br>• Performance of the Data Centre (PUE/WUE/CUE).<br>• Inventory of IT equipment used to deliver the cloud services.<br>• Type of servers (CPU/RAM) used in the service.<br>• Is equipment refurbished or not?<br>• The footprint of the servers and other IT equipment must be declared with a specific LCA provided by equipment suppliers.<br>• Quantity of e-Waste/WEEE generated each year. | P1 | 10 |

## 6.3 What is the CSP’s renewable energy policy? What is the transparency and traceability level of its GHG reporting in respect of its renewable energy purchases? {#q6-3}

### Rationale

- Renewable energy sourcing can be a lever to reduce its environmental footprint. Different types of contracts exist for this sourcing and their value is not equal considering criteria such as traceability of type of electricity generated (where, what kind of sources) and the synchronization between production and use. If the target of such a sourcing is to decarbonize its electrical mix the result must be computed and justified to prevent any kind of greenwashing.

### Evaluation criteria

| Evaluation criterion | Recommended priority | Proposed weighting (total = 10 points) |
|---|---|---|
| Proportions of electricity under PPA (Power Purchase Agreement), Guarantees of Origins (GoOs) or Renewable Energy Certificates (REC) are declared: % of PPA, % of GoOs/REC. | P1 | 3 |
| The emission factors used to convert electricity consumption into GHG emissions are declared and the computation of emissions is justified. This is easy for electricity procured under PPAs, but generally impossible for electricity covered by GoOs or RECs, except for GoOs associated with identified new renewable energy power plant and their precise type (photovoltaic, wind turbine or other) and location. It is not possible to justify an emission factor of zero, when we take an approach LCA in line with ISO 14001. | P1 | 3 |
| The CSP is asked to declare the proportion of the electricity that it uses that comes from renewable sources. | P2 | 2 |
| If the CSP cannot clearly justify segregation of consumption under PPAs and GoOs/RECs, market-based reporting must not be used and only location-based reporting may be used. | P2 | 2 |

## 6.4 How are Sovereignty and Resiliency considered in the cloud hosting policy? {#q6-4}

### Rationale

- Recent crises have proven how far the economy and the way of living of citizens can be impacted if national and regional sovereignty is not ensured, compromising people resiliency. These two concepts must be pillars of the digitalization strategy, with the objective to reduce its risk exposure and dependency, keeping a vigilant watch on financial expenses.

### Evaluation criteria

| Evaluation criterion | Recommended priority | Proposed weighting (total = 11 points) |
|---|---|---|
| The selection of the CSP takes into account: sovereignty and resiliency. Cloud agnostic architectures and solutions are deployed. Open Source solutions are highly promoted. | P1 | 3 |
| The storage and usage of data on cloud services respect the European GDPR regulations. | P1 | 3 |
| The data used and stored on cloud services are stored in identified locations and regions for the data centre, making it possible to identify applicable local regulations. For example: Patriot and Cloud Acts in the USA. | P2 | 1 |
| The cybersecurity protection level, the Business Continuity Plan and Disaster Recovery Plan, the financial costs and the environmental impacts of the SLA, are assessed and challenged. | P2 | 1 |
| Rebound effects are avoided by challenging the number of users of the services, and justifying the real value for the organisation of the cloud services delivered. | P2 | 1 |
| The financial cost of cloud services is charged back to end users. Here we have clear convergence between “FinOps” and “GreenOps”. | P2 | 1 |
| The end user is informed about the footprint of the cloud services he uses. | P2 | 1 |

As a CSP operates Data Centres and is connected to its client through its LAN and the external WAN, a large part of the questions and criteria in the Chapter 5 shall apply and should be requested of their NSP and their CSP by end users. Rationales are like the Chapter 5 and are not duplicated here.

## 6.5 How is Sustainable IT integrated to the design and management of the CSP’s data centres, infrastructures and facilities? {#q6-5}

### Evaluation criteria

| Evaluation criterion | Recommended priority | Proposed weighting (total = 17 points) |
|---|---|---|
| The CSP has taken into account the energy, environmental and societal performance during the Calls for Tender and the design phase, including the location. For example: installation on land that was already developed, proximity to facilities (offices, swimming pools, etc.) needing low temperature air, selection of eco-responsible materials. | P1 | 1.5 |
| The CSP must indicate its action plan for conformance with national regulations in the respect of performance. Example: “Décret Tertiaire” in France. | P1 | 1.5 |
| The CSP is able to declare a PUE for each Data Centre used in the cloud services that it delivers to a customer. It declares the methodology that it has adopted for computation (ISO standard for example). The means of measurement and the granularity of measurements, must be declared, differentiating real measurements from estimations, and specifying the nature of consumption covered (cooling, electrical losses, lighting, warming of oil for diesel generators, etc.). For example, the EN 50600-4-2 standard defines different levels of PUE according to data availability: PUE1, PUE2, PUE3. | P1 | 1.5 |
| Referring to the ADEME PCR “Methodological standard for the environmental assessment of Datacenter IT hosting services and cloud services”, the declaration of other indicators is also requested: WUE, ERF and REF. These indicators are mandatory to prevent impacts transfer, for example from energy consumption and GHG emissions to water by using evaporative cooling technologies. | P1 | 1.5 |
| Global consumption (energy, water, refrigerant gas leakages) must be reported at least quarterly in order to avoid drifts. | P1 | 1.5 |
| The Data Center owner shall indicate how many times the data or systems are duplicated for back-up and security policy. | P1 | 1.5 |
| The CSP shall indicate whether its data centre conforms to environmental building standards, such as BREAM or LEED. | P2 | 1 |
| The CSP knows and respects European regulation about reporting: https://ec.europa.eu/info/law/better-regulation/have-yoursay/initiatives/13818-Data-centres-in-Europe-reportingscheme_en | P2 | 1 |
| The PUE is declared with information that enables the estimation of performance: location (or external annual average temperature), Tiering level (for security, as defined by the Uptime Institute), the age of the Data Centre, the IT load (proportion of real power used for IT including network and servers, compared to the maximum capacity). | P2 | 1 |
| Data centers are designed for a maximum external air temperature. This information must be declared in order to anticipate any degradation of operational security induced by global warming. | P2 | 1 |
| The PUE shall be declared with a reference curve - PUE as a function of IT load – in order to enable comparison of measured values to theoretical ones (corrected from external temperature effects). | P2 | 1 |
| This curve shall have been verified at the delivery of the Data Centre, using variable resistances in place of servers in the bays. The measure should be done with an external temperature representative of an average annual air temperature. | P2 | 1 |
| The conclusions of regulatory energy audits shall be declared to clients with proof that they are used to define the masterplan for the rationalization of the pool of data centers. | P2 | 1 |
| The CSP initiative has been endorsed in a public engagement. E.g. signature on EU Code of Conduct (for Data Centre). | P3 | 0.25 |
| The CSP initiative is also extended to its stakeholders and suppliers. | P3 | 0.25 |
| The PUE should be reported quarterly at least, and this reporting and its frequency should be contractual. | P3 | 0.25 |
| For Fire protection systems: low-impact technologies are deployed; for example: fogging instead of FM200 gas. | P3 | 0.25 |

## 6.6 How is Sustainable IT integrated into the design and management of the CSP’s internal network (LAN) infrastructures and facilities? {#q6-6}

### Evaluation criteria

| Evaluation criterion | Recommended priority | Proposed weighting (total = 4 points) |
|---|---|---|
| The CSP must indicate whether its data centre embeds a network backbone and whether the energy consumption of this backbone is included in the PUE computation or not. | P2 | 2 |
| The energy consumption of the network (Local Area Network) must be identified and segregated from other sources of consumption, with specific means. | P2 | 2 |

## 6.7 How is sustainable IT integrated to the selection and management of data centres’ physical assets (servers)? {#q6-7}

### Evaluation criteria

| Evaluation criterion | Recommended priority | Proposed weighting (total = 14 points) |
|---|---|---|
| The energy consumption of servers must be identified and differentiated from other sources of consumption, with specific means (for example PDU). | P1 | 1.75 |
| Relevant eco-labels must be requested in the Calls for Tender for servers. EPEAT, TCO are recommended. 80+ and Energy star, which consider only energy performance are not sufficient. It is highly recommended to request a label of type 1 as defined in the ISO14024 standard. | P1 | 1.75 |
| The DPP (Digital Product Passport) is requested and considered in the selection process. It must be produced in conformance with the framework of the DPP EU regulation published on the 13th of June 2024 “setting of eco-design requirements for sustainable products”. | P1 | 1.75 |
| The Configuration Management Databases (CMDB) used to manage the allocation of servers, and the digital services, must cover all servers and link digital services to the hardware used to operate them. It must be up to date. | P1 | 1.75 |
| Unused machines and virtual machines must be identified and their detection shall trigger a decommissioning process, involving end users. | P1 | 1.75 |
| The lifespan of servers must be known and declared. | P1 | 1.75 |
| ASHRAE standards (A3 minimum, and A4 highly recommended) shall be requested in order to enable a higher temperature in cold aisle containment, and a wider range of humidity. | P2 | 0.5 |
| Urbanization must be done to avoid hot points that will require a reduction of setting of blown cold air. | P2 | 0.5 |
| The efficiency of urbanization should be verified regularly (no cold air leakages, no hot point), with specific means such as thermal cameras. | P2 | 0.5 |
| Virtualization of servers shall be deployed, and the virtualization rate shall be monitored. | P2 | 0.5 |
| The use of refurbished servers shall be promoted. | P2 | 0.5 |
| The CSP shall adopt scalability technologies and train its staff in them in order to enable the highest optimization of server usage. | P2 | 0.5 |
| The lifespan of servers shall be at least 7 years and 10 years are possible and recommended. | P3 | 0.25 |
| The Data Center owner shall indicate how many times the network systems are duplicated for back-up and security policy. | P3 | 0.25 |

A Wide Area Network (WAN) Service Provider is called an NSP in this chapter.

## 6.8 How do you assure the environmental reporting requested from your NSP, as a client? What data points are reported? How do you provide this reporting, if you are a NSP? {#q6-8}

### Evaluation criteria

| Evaluation criterion | Recommended priority | Proposed weighting (total = 6 points) |
|---|---|---|
| Emissions under all scopes (1, 2 and 3 of the GHG Protocol) are requested from the NSP (or provided by the organisation if it is an NSP). | P1 | 3 |
| The reporting requested (or provided) must include not only GHG emissions (including fugitive emissions of coolant, for example), but also other environmental impacts:<br>• Water consumption and WUE indicator<br>• CO₂ equivalent emissions and CUE indicator<br>• Depletion of mineral abiotic resources<br>• Primary Energy consumption<br>• Land use.<br>• And other relevant impacts necessary to evaluate impacts on biodiversity, in line with CSRD: acidification of soils and water, eutrophication, etc. | P1 | 3 |

## 6.9 How does the NSP provide LCA input data? {#q6-9}

### Evaluation criteria

| Evaluation criterion | Recommended priority | Proposed weighting (total = 3 points) |
|---|---|---|
| Input data for a Life Cycle Assessment of any digital service that uses WAN must be requested of the NSP (or provided by the NSP). For example:<br>• Average lifetime of network equipment.<br>• Inventory of infrastructures used by the network (wires, fiber)<br>• Annual consumptions of energy, water and coolant, are provided.<br>• Inventory of IT equipment used to deliver the network services.<br>• Bandwidth used to deliver the services.<br>• Is equipment refurbished or not?<br>• The footprint of the network equipment shall be declared with specific LCAs provided by equipment suppliers.<br>• Quantity of e-Waste/WEEE generated each year. | P1 | 3 |

## 6.10 What is the NSP’s renewable energy policy? What is the transparency and traceability level on its GHG reporting in respect of renewable energy purchase? {#q6-10}

### Evaluation criteria

| Evaluation criterion | Recommended priority | Proposed weighting (total = 6 points) |
|---|---|---|
| Proportions of electricity under PPA (Power Purchase Agreement), Guarantees of Origins (GoOs) or Renewable Energy Certificates (REC) are declared: % of PPA, % of GoOs/REC. | P1 | 2 |
| The emission factors used to convert electricity consumption into GHG emissions are declared and the computation of emissions is justified. (This is easy for electricity procured under PPAs, but generally impossible for electricity covered by GoOs or RECs, except for GoOs associated with new renewable energy power plant and their precise type (photovoltaic, wind turbine or other) and location. It is not possible to justify an emission factor of zero, when we take an approach to LCA in line with ISO 14001. | P1 | 2 |
| The NSP is asked to declare the proportion of the electricity that it uses that comes from renewable energy sources. | P2 | 1 |
| If the NSP cannot clearly justify segregation of consumption under PPAs and GoOs/RECs, market-based reporting must not be used and only location-based reporting may be used | P2 | 1 |

## 6.11 What actions are taken to reduce the footprint of WAN equipment? {#q6-11}

### Evaluation criteria

| Evaluation criterion | Recommended priority | Proposed weighting (total = 9 points) |
|---|---|---|
| Relevant eco-labels are requested for selected network equipment. Currently TCO seems to be the only eco-label for network equipment. 80+ and Energy star, which consider only energy performance, are not sufficient. It is highly recommended to ask for a label of type 1 as defined in the ISO14024 standard. | P1 | 3 |
| The consumption of electricity by network equipment should be drastically reduced when bandwidth is low (during nights and weekends). Proportional consumption with low threshold, deep sleeping modes. | P2 | 2 |
| The lifespan of network equipment must be known and declared. | P2 | 2 |
| The DPP (Digital Product Passport) is requested and considered in the selection process. It must conform to the framework of the DPP EU regulation published on 13th June 2024, “Setting of eco-design requirements for sustainable products”. | P3 | 1 |
| The obsolescence of network equipment is reduced, and its lifespan increased. | P3 | 1 |
