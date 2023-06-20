args = commandArgs(trailingOnly=TRUE)
if (length(args) != 1) {
    stop("One argument is needed", call.=FALSE)
}
id = args[1]
greet <- "Hello, I am running an R script for the"
print(cat(greet, id, "time."))
