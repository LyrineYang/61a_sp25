create table ints as
  select "zero"  as word, 1 as one, 0 as two, 0 as four, 0 as eight union
  select "one"          , 1        , 0        , 0         , 0          union
  select "two"          , 0        , 2        , 0         , 0          union
  select "three"        , 1        , 2        , 0         , 0          union
  select "four"         , 0        , 0        , 4         , 0          union
  select "five"         , 1        , 0        , 4         , 0          union
  select "six"          , 0        , 2        , 4         , 0          union
  select "seven"        , 1        , 2        , 4         , 0          union
  select "eight"        , 0        , 0        , 0         , 8          union
  select "nine"         , 1        , 0        , 0         , 8;
  