$directories = @(
    "app",
    "app\static",
    "app\templates",
    "app\main",
    "app\auth",
    "app\api",
    "migrations",
    "tests"
)

foreach ($dir in $directories) {
    mkdir $dir
}
