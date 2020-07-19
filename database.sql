create table teams (
    team_id integer not null,
    team_name varchar(255) unique not null,
    team_password varchar(255) not null,
primary key (team_id)
    );

create table tests (
    test_id integer not null,
    test_in text not null,
    test_out text not null,
    test_points integer not null,
    test_time integer not null,
    problem_id text not null,
    problem_logs boolean default false,
primary key (test_id)
    );

create table submissions (
    test_id integer not null,
    team_id integer not null,
    status integer not null,
    submission_date timestamp not null default CURRENT_TIMESTAMP,
    execution_time real not null,
primary key(test_id, team_id)
    );

create table problems (
    problem_id integer not null,
    problem_name varchar(255) not null,
    problem_description text,
    problem_difficulty integer not null,
primary key(problem_id)
    );

create table contest_data (
    contest_start integer not null,
    contest_deadline integer not null
    );
