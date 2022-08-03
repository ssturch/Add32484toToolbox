CREATE TABLE GOST_CFG_BS_SET_32484_3(
	Grid_Item_Number INTEGER,
	Grid_Item_Name TEXT,
	Grid_Item_Type TEXT,
	Controller INTEGER,
	Dimension TEXT,
	NoUnitConversion INTEGER,
	AltDataSource TEXT,
	ValueList TEXT,
	RelationField TEXT,
	OnFeatures TEXT,
	OffFeatures TEXT,
	OrderBy TEXT,
	ParameterID TEXT);
CREATE TABLE "GOST_DATA_BS_SET_32484_3"(
	"Size" TEXT,
	Bdk TEXT,
	Bk TEXT,
	Bs TEXT,
	Bdw TEXT,
	Bd TEXT,
	Nm TEXT,
	Ns TEXT,
	Ndw TEXT,
	CBORE_DIA TEXT,
	CBORE_DEPTH TEXT,
	enabled INTEGER,
	"key" INTEGER NOT NULL);
CREATE TABLE "GOST_DATA_BS_SET_32484_3_DISPLAY"(
	"STYLE" TEXT,
	ABBREV TEXT,
	OnFeatures TEXT,
	OffFeatures TEXT,
	IspCode TEXT,
	Description TEXT,
	enabled INTEGER,
	"key" INTEGER);
CREATE TABLE GOST_DATA_BS_SET_32484_3_LENGTHS(
	"Size" TEXT,
	Bl TEXT,
	Blg TEXT,
	enabled INTEGER,
	"key" INTEGER);
CREATE TABLE "GOST_DATA_BS_SET_32484_3_LENGTHS_PACKAGE" (
	"Size" TEXT,
	Bl TEXT,
	Blg TEXT,
	PckgThk TEXT,
	enabled INTEGER,
	"key" INTEGER NOT NULL);
CREATE TABLE GOST_DATA_BS_SET_CLIMATIC (
	ClimType TEXT,
	"key" INTEGER NOT NULL,
	enabled INTEGER
, ClimDesc TEXT);
CREATE TABLE GOST_DATA_BS_SET_COVER (
	CoverType TEXT,
	CoverKey INTEGER,
	enabled INTEGER);
CREATE TABLE GOST_DATA_BS_SET_COVERDESC (
	CoverKey INTEGER,
	CoverDesc TEXT,
	enabled INTEGER
, CoverDescForUser TEXT);
CREATE TABLE GOST_DATA_BS_SET_DURAB (
	StrClass TEXT,
	enabled INTEGER,
	"key" INTEGER
, StrClassForFilename TEXT);
CREATE TABLE GOST_TYPE_BS_SET(
	ID TEXT,
	enabled INTEGER,
	Protected INTEGER,
	Name TEXT,
	Title TEXT,
	Filename TEXT,
	PartUnits TEXT,
	ConfigurationTable TEXT,
	DataTable TEXT,
	DataTableUnits TEXT,
	DataTableSortField TEXT,
	PartNumberID TEXT,
	OrderID INTEGER,
	StackComponent INTEGER,
	SWConst_Enum_Value INTEGER,
	HoleDescriptionFormat TEXT,
	ValidHoleTypes INTEGER,
	HasHoles INTEGER,
	AltFilename TEXT,
	GlobalLengthPartNums INTEGER,
	"key" INTEGER);


