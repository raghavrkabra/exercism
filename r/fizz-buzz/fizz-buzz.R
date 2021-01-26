fizz_buzz <- function(input) {
  series <- c(1:input)
  for (i in series ) {
    if (i %% 3 == 0 && i %% 5 == 0) {
      series[i] <- 'Fizz Buzz';
    }
    else if (i %% 5 == 0) {
      series[i] <- 'Buzz';
    }
    else if (i %% 3 == 0) {
      series[i] <- 'Fizz';
    }
  }
  return(as.character(series));
}
