leap <- function(year) {
  # a leap year is a year that is divisible by 4 except century years
  # in their case is should be divisible by 400
  return( (year %% 4 == 0) & (year %% 100 != 0) | (year %% 400 == 0) )
}
