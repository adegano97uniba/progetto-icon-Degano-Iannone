%dataset -----------------------------------------------------------------------

city(bari,[bosch, peroni]).
city(napoli,[kimbo]).
city(roma,[amazon, as_roma]).
city(milano,[dng,mediolanum]).
city(torino,[fiat, sky]).

business(fiat,[it, marketing]).
business(bosch, [production, design]).
business(amazon, [logistic, web_services]).
business(dng, [dressmaking, marketing, distribution]).
business(mediolanum, [loans, trades]).
business(peroni, [production, distribution]).
business(kimbo, [farming, distribution]).
business(as_roma, [sport, market]).
business(sky, [sport, cinema, it]).

department(fiat,it, karl_kristiansen, [devops, helpdesk]).
department(fiat,marketing, bill_jackson, [acquisitions, budget]).
department(dng,marketing, quirino_greco, [social_media, tv_spot]).
department(bosch, production, abelardo_cremonesi, [build, assembly]).
department(bosch, design, marina_sagese, [functional, aesthetics]).
department(amazon, logistic, leo_toscani, [packaging, transport]).
department(amazon, web_services, savino_ferri, [marketplace, prime]).
department(dng, dressmaking, jole_lucciano, [drapery, cutting, sewing]).
department(dng, distribution, gabriele_romani, [d_europe, d_asia, d_america]).
department(mediolanum, loans, enza_derose, [applications, granted]).
department(mediolanum, trades, luigi_cocci, [security, invest]).
department(peroni, production, danilo_cagnin, [fermentation, bottling, labeling]).
department(peroni, distribution, gianni_pennetta, [internal, export]).
department(kimbo, farming, federica_albertini, [growing, harvest]).
department(kimbo, distribution, ignazio_mogherini, [d_s_italy,d_c_italy,d_n_italy]).
department(as_roma, sport, antonio_turci, [first_team, academy]).
department(as_roma, market, pasquale_scalera, [sales, engagements]).
department(sky, sport, ruggero_orlando, [football, basket, news]).
department(sky, cinema, fortunata_sauli, [on_demand, live]).
department(sky, it, giovanni_molesini, [app, website]).

group(budget, enzo_govoni, [gino_angeli, fausto_donati]).
group(devops, toni_bazzi , [michele_desantis, antonio_damato]).
group(social_media, deodato_arcuri, [rodrigo_costa, cassandra_buccho]).
group(tv_spot, gianni_lettiere, [livia_costanzi, lucia_ropea]).
group(build, linda_lucchesi, [ivan_manna, iolanda_piazza, elena_zola]).
group(assembly, giordana_zetticci, [gregorio_padovano, milena_sagese]).
group(functional, imelda_pinto, [gustavo_palerma, eufrosina_trevisani]).
group(aesthetics, prudenzia_fanucci, [eleonora_manna, isotta_chiavone, maria_stein, monica_ponti]).
group(packaging, filomena_siciliano, [ludovico_lucciano, silvio_lori]).
group(transport, demetrio_pisani, [pasqualina_ferri, dionisia_greece, mauro_comeriato]).
group(marketplace, enzo_bruno, [anita_napolitani, giuseppa_sabbatini]).
group(prime, augusto_marcelo, [rosina_bianchi, leardo_calabresi]).
group(drapery, mareta_siciliani, [valeria_lombardo, consuelo_arcuri, daria_tasso]).
group(cutting, averardo_pisano, [arturo_udinesi, lorenza_udinesi]).
group(sewing, fantino_zito, [oliviero_ferri, vitale_udinesi]).
group(d_europe, fioretta_marcelo, [isaia_calabresi, violante_fallaci, melissa_maspero, gilberto_solimena]).
group(d_asia, lia_trentino, [norberto_fiorentino, alberta_castiglione]).
group(d_america, calimero_lombardo, [lodovica_endrizzi, rufino_ricci, rita_borsellino]).
group(applications, stella_angelo, [isauro_lombardi, arsenio_udinesi]).
group(granted, mareta_romani, [sesto_davide, ortensio_trevisano, armando_civaschi]).
group(security, eros_giordano, [carmela_fallaci, amelia_baresi]).
group(invest, concetta_bergamaschi, [rosaura_lettiere, deborah_greece]).
group(fermentation, lidia_marino, [anita_brugnaro, paulina_roselli, alessandra_turchi, gaspare_bettoni]).
group(bottling, ludovico_pigafetta, [toni_toninelli , luciano_gemito]).
group(labeling, filippo_deledda, [livia_turati, ansaldo_villarosa]).
group(internal, vittorio_palombi, [gioachino_polizzi, alberto_montessori]).
group(export, benvenuto_gabrieli, [marissa_bignami, giuliana_bergoglio, jacopo_maggioli]).
group(growing, liliana_botta , [adelmo_arano, greco_acomio]).
group(harvest, flavia_pasqua, [cassandra_piane, gaetano_filangieri]).
group(d_s_italy, olga_draghi, [michela_viola, cristina_salandra]).
group(d_c_italy, fedele_panatta, [daniele_ariasso, eugenia_carpaccio]).
group(d_n_italy, claudia_pedroni, [mattia_zanichelli, guglielmo_calarco, vincenza_gaiatto]).
group(first_team, ninetta_moresi, [calcedonio_franscini, rosa_dalla, giampiero_franceschi, beppe_vassoni, flavio_piccinni]).
group(academy, cecilia_torricelli, [letizia_romiti, lauretta_fuseli, carmelo_ferragamo, costantino_erquiglini]).
group(sales, licia_gemito, [ettore_carli, roberta_roero]).
group(engagements, pierina_trussardi, [fausto_crespi, franco_niggli]).
group(football, manolo_parpinel, [elena_giacometti, milo_leone, maria_gostinelli]).
group(basket, antonio_cruso, [bianca_roth , tiziana_desio]).
group(news, fiorino_iannuzzi, [licia_malotelli, roberto_abbagnale, pierangelo_vianello, vittoria_udinesi]).
group(on_demand, fernanda_bonomo, [lilla_leonetti, franco_dalosio, rocco_carriera]).
group(live, daniele_vantozzi, [daniele_dossetti, agostino_altarossa, federico_bernardi, beatrice_vergassola]).
group(app, iolanda_musatti, [benedetto_napolitano, vincenza_schiavo, carla_tozzo]).
group(website, benedetto_filogamo, [allegra_cherubini , filippo_iannotti, luciano_vattimo]).

%menu ---------------------------------------------------------------------

/*start Rule*/
start:-
      write('*** Full Business organization knowledge base  ***'),nl,nl,
      write('** Our system will allow you to extract knowledge from a city-business-department-group based database **'),nl,
      menu.
/*Main menu rule*/
menu:- 
     nl,nl,
     write('Available functions:"'),nl,
     write('1- Check if two people are coworkers'),nl,
     write('2- Check if an empoloyee is a department manager, given department name'),nl,
     write('3- Check if an employee is a group leader'),nl,
     write('4- Find the head Boss of an employee'),nl,
     write('5- Check if a business belongs to a city'),nl,
     write('6- Check if a department belongs to a business'),nl,
     write('7- Check if a group belongs to a department'),nl,
     write('8- Check if an employee belongs to a group'),nl,
     write('9- Check if somebody belongs to a business'),nl,
     write('10- Given a group, list all other groups in a department'),nl,
     write('11- List all heads of department of a given business'),nl,
     write('12- List all the groups of a department'),nl,
     write('13- List all the members of a group'),nl,
     write('14- List all businesses present in a given city'),nl,
     write('15- List all group leaders of a business'),nl,
     write('16- List all the employees of a business'),nl,nl,

write('NOTE: Always write a full stop before submitting your choices and information.'),nl,
write('NOTE: Always use underscores (_) for spaces.'),nl,
write('NOTE: If your query returns a red "false", type start. to continue.'),nl,
write('NOTE: Do not use uppercase letters.'),nl,nl,

write('Enter your choice:'),nl,
read(X),
option(X).

/*second menu rule*/
menutwo:-
nl,nl,
write('Do you want to continue? "Select 17 or 18'),nl,
write('17- Yes'),nl,
write('18- No'),nl,

write('NOTE: Always write a full stop before submitting your choices and information.'),nl,
write('NOTE: Always use underscores (_) for spaces.'),nl,
write('NOTE: If your query returns a red "false", type start. to continue.'),nl,
write('NOTE: Do not use uppercase letters.'),nl,nl,

write('Enter your choice:'),nl,
read(X),
option(X).

%rules -------------------------------------------------------------------------
employee(Group,Groups) :- group(Group,_,Groups).

%coworker check
coworker(Name,Department,none) :- department(_,Department,Name,_).
coworker(Name, Department, Group) :- department(_,Department,_,Groups),
									employee(Group,Groups),
									group(Group,Name,_).

coworker(Name,Name2,Department,Group) :-
    department(_,Department,_,Groups),
    member(Group,Groups),
    group(Group,_,People),
    member(Name,People),
    member(Name2,People).

coworkerCore(Name1,Name2,Group):-
	group(Group,_,Employees),
	member(Name1,Employees),
	member(Name2,Employees).

coworker(Name1,Name2):-
	coworkerCore(Name1,Name2,_).

option(1):-
    write('Insert the first employee name'),nl,
    read(Name),
    write('Insert the second employee name'),nl,
    read(Name2),
	coworker(Name,Name2)-> write('true'),
    menutwo.

%department manager check
manager(Name, Department) :- department(_,Department,Name,_).
manager(Name, Group) :- group(Group, Name, _).

option(2):-
    write('Insert the employee name'),nl,
    read(Name),
    write('Insert the department name'),nl,
    read(Department),
	manager(Name, Department)-> write('true'),
    menutwo.
    

%group leader check
leader(Name, Group) :- group(Group,Name,_).

option(3):-
    write('Insert the employee name'),nl,
    read(Name),
    write('Insert the group name'),nl,
    read(Group),
	leader(Name, Group)-> write('true'),
    menutwo.

	
%head boss search
bossOf(Employee):-
	workerBusinessCore(Employee,Group,Department,_),
	department(_,Department,_,Groups),
	member(Group,Groups),
	findall(Boss,department(_,Department,Boss,Groups),Boss),write(Boss).
	


option(4):-
    write('Insert the employee name'),nl,
    read(Employee),
	bossOf(Employee),
    menutwo.

%business city presence check
businessBelongs(Business,City) :-
    city(City,Businesses),
    member(Business,Businesses).

option(5):-
    write('Insert the business name'),nl,
    read(Business),
    write('Insert the city name'),nl,
    read(City),
	businessBelongs(Business,City)-> write('true'),
    menutwo.

%department belonging to business check
departmentBelongs(Department,Business) :-
    			business(Business,Departments),
    			member(Department,Departments).

option(6):-
    write('Insert the department name'),nl,
    read(Department),
    write('Insert the business name'),nl,
    read(Business),
	departmentBelongs(Department,Business)-> write('true'),
    menutwo.

%group belonging to department check        
groupBelongs(Group,Department) :-
    department(_,Department,_,Groups),
    member(Group,Groups).
	
groupBelongs(Group,Department,Business) :-
	department(Business,Department,_,Groups),
    member(Group,Groups).

option(7):-
    write('Insert the group name'),nl,
    read(Group),
    write('Insert the department name'),nl,
    read(Department),
	write('Insert the business name'),nl,
    read(Business),
	groupBelongs(Group,Department,Business)-> write('true'),
    menutwo.

%worker belonging to group check
workerBelongs(Employee,Group) :-
    group(Group,_,Employees),
    member(Employee,Employees);
	group(Group,Employee,_).

option(8):-
    write('Insert the employee name'),nl,
    read(Employee),
    write('Insert the group name'),nl,
    read(Group),
	workerBelongs(Employee,Group)-> write('true'),
    menutwo.

%core waterfall search function employee to business
workerBusinessCore(Employee,Group,Department,Business):-
    workerBelongs(Employee,Group),
    groupBelongs(Group,Department),
    departmentBelongs(Department,Business).

%worker belonging to business check
workerBusiness(Employee,Business):-
    workerBusinessCore(Employee,_,_,Business);
	department(Business,_,Employee,_);
	workerBusinessCore(Employee,_,_,Business),
	department(Business,Department,_,Groups),
	group(Group,Employee,_),
	member(Group,Groups).

option(9):-
    write('Insert the employee name'),nl,
    read(Employee),
    write('Insert the business name'),nl,
    read(Business),
	workerBusiness(Employee,Business)-> write('true'),
    menutwo.
  

groupBelongs(Group,Department,Business) :-	
    department(Business,Department,_,Groups),
    member(Group,Groups).
	
%list all other groups in a department
listDepartmentGroups(Group,Department,Business):-

    groupBelongs(Group,Department,Business)->  findall(Groups,department(Business,Department,_,Groups),Groups),
    write(Groups).

option(10):-
    write('Insert the group name'),nl,
    read(Group),
    write('Insert the department name'),nl,
    read(Department),
	write('Insert the business name'),nl,
    read(Business),
	listDepartmentGroups(Group,Department,Business),
    menutwo.

%list all business managers
listBusinessManagers(Business) :-
    departmentBelongs(_,Business)->  findall(Managers,department(Business,_,Managers,_),Managers),
    write(Managers).

option(11):-
    write('Insert the business name'),nl,
    read(Business),
	listBusinessManagers(Business),
    menutwo.

%list all department groups
listDepartmentGroups(Department,Business) :-
    findall(Groups,department(Business,Department,_,Groups),Groups),
    write(Groups).

option(12):-
    write('Insert the department name'),nl,
    read(Department),
	write('Insert the business name'),nl,
    read(Business),
	listDepartmentGroups(Department,Business),
    menutwo.

%list all group members
listGroupMembers(Group) :-
	findall(Leader,group(Group,Leader,_),Leader),
    write(Leader),
    findall(Members,group(Group,_,Members),Members),
    write(Members).
	

option(13):-
    write('Insert the group name'),nl,
    read(Group),
	listGroupMembers(Group),
    menutwo.

%list all city businesses
listCityBusinesses(City) :-
    findall(Businesses,city(City,Businesses),Businesses),
    write(Businesses).

option(14):-
    write('Insert the city name'),nl,
    read(City),
	listCityBusinesses(City),
    menutwo.

%list all business group leaders
listBusinessLeadersCore(Group,Department,Business,Leader) :-
    groupBelongs(Group,Department),
    departmentBelongs(Department,Business),
    group(Group,Leader,_),
	department(Business,Department,_,Groups),
	member(Group,Groups).
    
listBusinessLeaders(Business) :-
    findall(Leader,listBusinessLeadersCore(Group,_,Business,Leader),Leader),
    write(Leader).

option(15):-
    write('Insert the business name'),nl,
    read(Business),
	listBusinessLeaders(Business),
    menutwo.
    
%list all business employees
listBusinessEmployeesCore(Business,Department,Group,Leader,Manager,Employees) :-
    groupBelongs(Group,Department),
    departmentBelongs(Department,Business),
    group(Group,Leader,Employees),
    department(Business,Department,Manager,_).

listBusinessEmployees(Business) :-
    findall(Managers,department(Business,_,Managers,_), Managers),
    write(Managers),
    findall(Leaders,listBusinessEmployeesCore(Business,_,_,Leaders,_,_), Leaders),
    write(Leaders),
    findall(Employees,listBusinessEmployeesCore(Business,_,_,_,_,Employees), Employees),
    write(Employees).

option(16):-
    write('Insert the business name'),nl,
    read(Business),
	listBusinessEmployees(Business),
    menutwo.


option(17):-
    menu.

option(18):-
	halt.
  
