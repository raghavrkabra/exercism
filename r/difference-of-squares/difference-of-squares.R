sum_of_n_squares <- function(number) {
  return(number * (number + 1) * (number * 2 + 1) / 6)
}


sum_of_n <- function(number) {
  return(number * (number + 1) / 2)
}


# this function that takes a natural_number
# and should return the difference-of-squares as described
# in the README.md
difference_of_squares <- function(natural_number) {
  return(abs(sum_of_n_squares(natural_number) - sum_of_n(natural_number)^2))
}
