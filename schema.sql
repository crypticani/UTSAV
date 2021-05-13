BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "records_tabletennismodel" (
	"record_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"player1"	varchar(30) NOT NULL,
	"player2"	varchar(30) NOT NULL,
	"score_p1"	varchar(30) NOT NULL,
	"score_p2"	varchar(30) NOT NULL,
	"winner"	varchar(30) NOT NULL,
	"category_id"	integer NOT NULL,
	"event_id_id"	integer NOT NULL,
	FOREIGN KEY("event_id_id") REFERENCES "events_individualeventslist"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "registration_categories"("category_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "records_powerliftingmodel" (
	"record_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"player_name"	varchar(30) NOT NULL,
	"idnum"	integer NOT NULL,
	"weight"	varchar(10) NOT NULL,
	"result"	varchar(10) NOT NULL,
	"category_id"	integer NOT NULL,
	"event_id_id"	integer NOT NULL,
	FOREIGN KEY("event_id_id") REFERENCES "events_individualeventslist"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "registration_categories"("category_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "records_chessmodel" (
	"record_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"player1"	varchar(30) NOT NULL,
	"player2"	varchar(30) NOT NULL,
	"score_p1"	varchar(30) NOT NULL,
	"score_p2"	varchar(30) NOT NULL,
	"winner"	varchar(30) NOT NULL,
	"category_id"	integer NOT NULL,
	"event_id_id"	integer NOT NULL,
	FOREIGN KEY("event_id_id") REFERENCES "events_individualeventslist"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "registration_categories"("category_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "records_carrommodel" (
	"record_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"team1_player1"	varchar(30) NOT NULL,
	"team1_player2"	varchar(30) NOT NULL,
	"team2_player1"	varchar(30) NOT NULL,
	"team2_player2"	varchar(30) NOT NULL,
	"winner"	varchar(30) NOT NULL,
	"category_id"	integer NOT NULL,
	"event_id_id"	integer NOT NULL,
	FOREIGN KEY("event_id_id") REFERENCES "events_individualeventslist"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "registration_categories"("category_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "records_badmintonmodel" (
	"record_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"team1_player1"	varchar(30) NOT NULL,
	"team1_player2"	varchar(30) NOT NULL,
	"team2_player1"	varchar(30) NOT NULL,
	"team2_player2"	varchar(30) NOT NULL,
	"score"	varchar(10) NOT NULL,
	"winner"	varchar(30) NOT NULL,
	"category_id"	integer NOT NULL,
	"event_id_id"	integer NOT NULL,
	FOREIGN KEY("event_id_id") REFERENCES "events_individualeventslist"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "registration_categories"("category_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "records_athleticsmodel" (
	"record_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"event_name"	varchar(30) NOT NULL,
	"player_name"	varchar(30) NOT NULL,
	"idnum"	integer NOT NULL,
	"result"	varchar(10) NOT NULL,
	"category_id"	integer NOT NULL,
	"event_id_id"	integer NOT NULL,
	FOREIGN KEY("event_id_id") REFERENCES "events_individualeventslist"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "registration_categories"("category_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "registration_individualregistration" (
	"reg_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"year"	integer NOT NULL,
	"name"	varchar(100) NOT NULL,
	"course"	varchar(100) NOT NULL,
	"mobile"	varchar(10) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"event_id"	integer NOT NULL,
	"idnum"	varchar(6) NOT NULL,
	FOREIGN KEY("event_id") REFERENCES "registration_events"("tevent_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "events_teameventlist" (
	"id"	integer NOT NULL,
	"datetime"	datetime NOT NULL,
	"venue"	varchar(30) NOT NULL,
	"event_name_id"	integer NOT NULL,
	"team1_id"	integer NOT NULL,
	"team2_id"	integer NOT NULL,
	"year"	integer NOT NULL,
	FOREIGN KEY("team2_id") REFERENCES "registration_teamregistrationmodel"("reg_id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("team1_id") REFERENCES "registration_teamregistrationmodel"("reg_id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("event_name_id") REFERENCES "registration_events"("tevent_id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "events_individualeventslist" (
	"id"	integer NOT NULL,
	"fix"	varchar(100) NOT NULL,
	"datetime"	datetime NOT NULL,
	"venue"	varchar(100) NOT NULL,
	"category_id"	integer,
	"event_id"	integer NOT NULL,
	"year"	integer NOT NULL,
	FOREIGN KEY("event_id") REFERENCES "registration_events"("tevent_id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "registration_categories"("category_id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "registration_rules" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"is_active"	bool NOT NULL,
	"rule"	text NOT NULL
);
CREATE TABLE IF NOT EXISTS "records_teamrecordmodel" (
	"record_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"score_team1"	varchar(30) NOT NULL,
	"score_team2"	varchar(30) NOT NULL,
	"event_id_id"	integer NOT NULL,
	"winner_id"	integer NOT NULL,
	FOREIGN KEY("winner_id") REFERENCES "registration_teamregistrationmodel"("reg_id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("event_id_id") REFERENCES "events_teameventlist"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "main_imagegallery" (
	"img_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"image_name"	varchar(30) NOT NULL,
	"image"	varchar(100) NOT NULL,
	"folder_id_id"	integer NOT NULL,
	FOREIGN KEY("folder_id_id") REFERENCES "main_galleryfolder"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "main_profile" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"first_name"	varchar(100) NOT NULL,
	"last_name"	varchar(100) NOT NULL,
	"gender"	varchar(10) NOT NULL,
	"email"	varchar(150) NOT NULL,
	"mobile"	varchar(10) NOT NULL,
	"signup_confirmation"	bool NOT NULL,
	"course_id"	integer,
	"user_id"	integer NOT NULL UNIQUE,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("course_id") REFERENCES "main_courses"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "main_notice" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"content"	text NOT NULL,
	"date"	datetime NOT NULL,
	"is_active"	bool NOT NULL
);
CREATE TABLE IF NOT EXISTS "main_galleryfolder" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"folder_name"	varchar(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS "main_courses" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"course"	varchar(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS "registration_teamplayers" (
	"player_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"player_name"	varchar(30) NOT NULL,
	"id_number"	varchar(6) NOT NULL,
	"is_active"	bool NOT NULL,
	"team_id_id"	integer NOT NULL,
	FOREIGN KEY("team_id_id") REFERENCES "registration_permanentteam"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "registration_teamregistrationmodel" (
	"reg_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"year"	integer NOT NULL,
	"category_id"	integer,
	"team_name_id"	integer NOT NULL,
	FOREIGN KEY("team_name_id") REFERENCES "registration_permanentteam"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "registration_categories"("category_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "registration_permanentteam" (
	"id"	integer NOT NULL,
	"team_name"	varchar(30) NOT NULL,
	"captain"	varchar(30) NOT NULL,
	"vice_captain"	varchar(30),
	"email"	varchar(254) NOT NULL,
	"mobile"	varchar(10) NOT NULL,
	"event_name_id"	integer NOT NULL,
	FOREIGN KEY("event_name_id") REFERENCES "registration_events"("tevent_id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "registration_events" (
	"tevent_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"events"	varchar(20) NOT NULL,
	"type"	varchar(10) NOT NULL,
	"active"	bool NOT NULL,
	"category_id"	integer NOT NULL,
	FOREIGN KEY("category_id") REFERENCES "registration_categories"("category_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "registration_categories" (
	"category_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"category"	varchar(10) NOT NULL
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(150) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag">=0),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL
);
CREATE INDEX IF NOT EXISTS "records_tabletennismodel_event_id_id_d899afda" ON "records_tabletennismodel" (
	"event_id_id"
);
CREATE INDEX IF NOT EXISTS "records_tabletennismodel_category_id_5a9720ed" ON "records_tabletennismodel" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "records_powerliftingmodel_event_id_id_dc9cc6fa" ON "records_powerliftingmodel" (
	"event_id_id"
);
CREATE INDEX IF NOT EXISTS "records_powerliftingmodel_category_id_7a001347" ON "records_powerliftingmodel" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "records_chessmodel_event_id_id_9c98f2b4" ON "records_chessmodel" (
	"event_id_id"
);
CREATE INDEX IF NOT EXISTS "records_chessmodel_category_id_92aa54eb" ON "records_chessmodel" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "records_carrommodel_event_id_id_2abb0b8d" ON "records_carrommodel" (
	"event_id_id"
);
CREATE INDEX IF NOT EXISTS "records_carrommodel_category_id_70bb669c" ON "records_carrommodel" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "records_badmintonmodel_event_id_id_7c35f15a" ON "records_badmintonmodel" (
	"event_id_id"
);
CREATE INDEX IF NOT EXISTS "records_badmintonmodel_category_id_8418987d" ON "records_badmintonmodel" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "records_athleticsmodel_event_id_id_13eeab18" ON "records_athleticsmodel" (
	"event_id_id"
);
CREATE INDEX IF NOT EXISTS "records_athleticsmodel_category_id_91b923bc" ON "records_athleticsmodel" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "registration_individualregistration_event_id_01ac1426" ON "registration_individualregistration" (
	"event_id"
);
CREATE INDEX IF NOT EXISTS "events_teameventlist_team2_id_98529d20" ON "events_teameventlist" (
	"team2_id"
);
CREATE INDEX IF NOT EXISTS "events_teameventlist_team1_id_3ef7d248" ON "events_teameventlist" (
	"team1_id"
);
CREATE INDEX IF NOT EXISTS "events_teameventlist_event_name_id_a8d07b30" ON "events_teameventlist" (
	"event_name_id"
);
CREATE INDEX IF NOT EXISTS "events_individualeventslist_event_id_a8d48192" ON "events_individualeventslist" (
	"event_id"
);
CREATE INDEX IF NOT EXISTS "events_individualeventslist_category_id_3d15af44" ON "events_individualeventslist" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "records_teamrecordmodel_winner_id_88258413" ON "records_teamrecordmodel" (
	"winner_id"
);
CREATE INDEX IF NOT EXISTS "records_teamrecordmodel_event_id_id_3a3860cc" ON "records_teamrecordmodel" (
	"event_id_id"
);
CREATE INDEX IF NOT EXISTS "main_gallerymodel_folder_id_id_02394e0f" ON "main_imagegallery" (
	"folder_id_id"
);
CREATE INDEX IF NOT EXISTS "main_profile_course_id_1195935e" ON "main_profile" (
	"course_id"
);
CREATE INDEX IF NOT EXISTS "registration_teamplayers_team_id_id_075452a9" ON "registration_teamplayers" (
	"team_id_id"
);
CREATE INDEX IF NOT EXISTS "registration_teamregistrationmodel_team_name_id_05aed0b1" ON "registration_teamregistrationmodel" (
	"team_name_id"
);
CREATE INDEX IF NOT EXISTS "registration_teamregistrationmodel_category_id_a6fa397c" ON "registration_teamregistrationmodel" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "registration_permanentteam_event_name_id_53a274e0" ON "registration_permanentteam" (
	"event_name_id"
);
CREATE INDEX IF NOT EXISTS "registration_events_category_id_d83cde8f" ON "registration_events" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
COMMIT;
