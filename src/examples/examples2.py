first = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
# first = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]
# 9 deadline: 15
# 10:30 deadline: 13, 14, 16, 20, 29, 30, 31, 34, 37, 40
# ^ Add 25 here?

second = [2, 3, 6, 8, 10, 12, 18, 21, 23, 25, 28, 32, 36, 38]
# Truck 2 requirement: 3, 18, 36, 38
# 9:05 arrival: 6, 25, 28, 32
# 10:30 deadline: 6, 25,

first_second = [4, 5, 7, 9, 11, 17, 22, 24, 26, 27, 33, 35, 39]
# first_second = [4, 5, 7, 9, 11, 17, 19, 22, 24, 26, 27, 33, 35, 39]
# 10:20 address correction: 9


first_truck = [
    [
        "1",
        "",
        "195 W Oakland Ave",
        "Salt Lake City",
        "UT",
        "84115",
        "10:30:00",
        "21",
        "None",
        "",
        "At hub",
    ],
    [
        "13",
        "",
        "2010 W 500 S",
        "Salt Lake City",
        "UT",
        "84104",
        "10:30:00",
        "2",
        "None",
        "",
        "At hub",
    ],
    [
        "14",
        "",
        "4300 S 1300 E",
        "Millcreek",
        "UT",
        "84117",
        "10:30:00",
        "88",
        "Must be delivered with 15 & 19",
        "",
        "At hub",
    ],
    [
        "15",
        "",
        "4580 S 2300 E",
        "Holladay",
        "UT",
        "84117",
        "9:00:00",
        "4",
        "None",
        "",
        "At hub",
    ],
    [
        "16",
        "",
        "4580 S 2300 E",
        "Holladay",
        "UT",
        "84117",
        "10:30:00",
        "88",
        "Must be delivered with 13 & 19",
        "",
        "At hub",
    ],
    [
        "20",
        "",
        "3595 Main St",
        "Salt Lake City",
        "UT",
        "84115",
        "10:30:00",
        "37",
        "Must be delivered with 13 & 15",
        "",
        "At hub",
    ],
    [
        "29",
        "",
        "1330 2100 S",
        "Salt Lake City",
        "UT",
        "84106",
        "10:30:00",
        "2",
        "None",
        "",
        "At hub",
    ],
    [
        "30",
        "",
        "300 State St",
        "Salt Lake City",
        "UT",
        "84103",
        "10:30:00",
        "1",
        "None",
        "",
        "At hub",
    ],
    [
        "31",
        "",
        "3365 S 900 W",
        "Salt Lake City",
        "UT",
        "84119",
        "10:30:00",
        "1",
        "None",
        "",
        "At hub",
    ],
    [
        "34",
        "",
        "4580 S 2300 E",
        "Holladay",
        "UT",
        "84117",
        "10:30:00",
        "2",
        "None",
        "",
        "At hub",
    ],
    [
        "37",
        "",
        "410 S State St",
        "Salt Lake City",
        "UT",
        "84111",
        "10:30:00",
        "2",
        "None",
        "",
        "At hub",
    ],
    [
        "40",
        "",
        "380 W 2880 S",
        "Salt Lake City",
        "UT",
        "84115",
        "10:30:00",
        "45",
        "None",
        "",
        "At hub",
    ],
]

second_truck = [
    [
        "2",
        "",
        "2530 S 500 E",
        "Salt Lake City",
        "UT",
        "84106",
        "EOD",
        "44",
        "None",
        "",
        "At hub",
    ],
    [
        "3",
        "",
        "233 Canyon Rd",
        "Salt Lake City",
        "UT",
        "84103",
        "EOD",
        "2",
        "Can only be on truck 2",
        "",
        "At hub",
    ],
    [
        "6",
        "",
        "3060 Lester St",
        "West Valley City",
        "UT",
        "84119",
        "10:30:00",
        "88",
        "Delayed on flight---will not arrive to depot until 9:05 am",
        "",
        "At hub",
    ],
    [
        "8",
        "",
        "300 State St",
        "Salt Lake City",
        "UT",
        "84103",
        "EOD",
        "9",
        "None",
        "",
        "At hub",
    ],
    [
        "10",
        "",
        "600 E 900 South",
        "Salt Lake City",
        "UT",
        "84105",
        "EOD",
        "1",
        "None",
        "",
        "At hub",
    ],
    [
        "12",
        "",
        "3575 W Valley Central Station bus Loop",
        "West Valley City",
        "UT",
        "84119",
        "EOD",
        "1",
        "None",
        "",
        "At hub",
    ],
    [
        "18",
        "",
        "1488 4800 S",
        "Salt Lake City",
        "UT",
        "84123",
        "EOD",
        "6",
        "Can only be on truck 2",
        "",
        "At hub",
    ],
    [
        "21",
        "",
        "3595 Main St",
        "Salt Lake City",
        "UT",
        "84115",
        "EOD",
        "3",
        "None",
        "",
        "At hub",
    ],
    [
        "23",
        "",
        "5100 South 2700 West",
        "Salt Lake City",
        "UT",
        "84118",
        "EOD",
        "5",
        "None",
        "",
        "At hub",
    ],
    [
        "25",
        "",
        "5383 South 900 East #104",
        "Salt Lake City",
        "UT",
        "84117",
        "10:30:00",
        "7",
        "Delayed on flight---will not arrive to depot until 9:05 am",
        "",
        "At hub",
    ],
    [
        "28",
        "",
        "2835 Main St",
        "Salt Lake City",
        "UT",
        "84115",
        "EOD",
        "7",
        "Delayed on flight---will not arrive to depot until 9:05 am",
        "",
        "At hub",
    ],
    [
        "32",
        "",
        "3365 S 900 W",
        "Salt Lake City",
        "UT",
        "84119",
        "EOD",
        "1",
        "Delayed on flight---will not arrive to depot until 9:05 am",
        "",
        "At hub",
    ],
    [
        "36",
        "",
        "2300 Parkway Blvd",
        "West Valley City",
        "UT",
        "84119",
        "EOD",
        "88",
        "Can only be on truck 2",
        "",
        "At hub",
    ],
    [
        "38",
        "",
        "410 S State St",
        "Salt Lake City",
        "UT",
        "84111",
        "EOD",
        "9",
        "Can only be on truck 2",
        "",
        "At hub",
    ],
]

first_truck_second_trip = [
    [
        "4",
        "",
        "380 W 2880 S",
        "Salt Lake City",
        "UT",
        "84115",
        "EOD",
        "4",
        "None",
        "",
        "At hub",
    ],
    [
        "5",
        "",
        "410 S State St",
        "Salt Lake City",
        "UT",
        "84111",
        "EOD",
        "5",
        "None",
        "",
        "At hub",
    ],
    [
        "7",
        "",
        "1330 2100 S",
        "Salt Lake City",
        "UT",
        "84106",
        "EOD",
        "8",
        "None",
        "",
        "At hub",
    ],
    [
        "9",
        "",
        "410 S State St",
        "Salt Lake City",
        "UT",
        "84111",
        "EOD",
        "2",
        "Wrong address listed",
        "",
        "At hub",
    ],
    [
        "11",
        "",
        "2600 Taylorsville Blvd",
        "Salt Lake City",
        "UT",
        "84118",
        "EOD",
        "1",
        "None",
        "",
        "At hub",
    ],
    [
        "17",
        "",
        "3148 S 1100 W",
        "Salt Lake City",
        "UT",
        "84119",
        "EOD",
        "2",
        "None",
        "",
        "At hub",
    ],
    [
        "19",
        "",
        "177 W Price Ave",
        "Salt Lake City",
        "UT",
        "84115",
        "EOD",
        "37",
        "None",
        "",
        "At hub",
    ],
    [
        "22",
        "",
        "6351 South 900 East",
        "Murray",
        "UT",
        "84121",
        "EOD",
        "2",
        "None",
        "",
        "At hub",
    ],
    [
        "24",
        "",
        "5025 State St",
        "Murray",
        "UT",
        "84107",
        "EOD",
        "7",
        "None",
        "",
        "At hub",
    ],
    [
        "26",
        "",
        "5383 South 900 East #104",
        "Salt Lake City",
        "UT",
        "84117",
        "EOD",
        "25",
        "None",
        "",
        "At hub",
    ],
    [
        "27",
        "",
        "1060 Dalton Ave S",
        "Salt Lake City",
        "UT",
        "84104",
        "EOD",
        "5",
        "None",
        "",
        "At hub",
    ],
    [
        "33",
        "",
        "2530 S 500 E",
        "Salt Lake City",
        "UT",
        "84106",
        "EOD",
        "1",
        "None",
        "",
        "At hub",
    ],
    [
        "35",
        "",
        "1060 Dalton Ave S",
        "Salt Lake City",
        "UT",
        "84104",
        "EOD",
        "88",
        "None",
        "",
        "At hub",
    ],
    [
        "39",
        "",
        "2010 W 500 S",
        "Salt Lake City",
        "UT",
        "84104",
        "EOD",
        "9",
        "None",
        "",
        "At hub",
    ],
]
