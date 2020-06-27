<p align="center">
  <h1 align="center">THEMA</h1>
  <p align="center">
    <a href="https://github.com/LuxAter/Thema/graphs/contributors"><img src="https://img.shields.io/github/contributors/LuxAter/Thema.svg?style=flat-square"></a>
    <a href="https://github.com/LuxAter/Thema/network/members"><img src="https://img.shields.io/github/forks/LuxAter/Thema.svg?style=flat-square"></a>
    <a href="https://github.com/LuxAter/Thema/stargazers"><img src="https://img.shields.io/github/stars/LuxAter/Thema.svg?style=flat-square"></a>
    <a href="https://github.com/LuxAter/Thema/issues"><img src="https://img.shields.io/github/issues/LuxAter/Thema.svg?style=flat-square"></a>
    <a href="https://github.com/LuxAter/Thema/blob/master/LICENSE.md"><img src="https://img.shields.io/github/license/LuxAter/Thema.svg?style=flat-square"></a>
    <a href="https://github.com/LuxAter/Thema/releases"><img src="https://img.shields.io/github/tag/LuxAter/Thema.svg?include_prereleases&sort=semver&style=flat-square"></a>
    <a href="https://github.com/LuxAter/Thema/actions?query=workflows%3ADevelopment"><img src="https://img.shields.io/github/workflow/status/LuxAter/Thema/Development.svg?include_prereleases&sort=semver&style=flat-square"></a>
    <br/>
    System wide theme configuration tool
    <br/>
    <a href="https://github.com/LuxAter/Thema/issues/new?template=bug_report.md">Report Bug</a>
    ·
    <a href="https://github.com/LuxAter/Thema/issues/new?template=feature_request.md">Request Feature</a>
  </p>
</p>

## About the Project

There are hundreds of different color schemes, and for an equally large number of
different programs. Thema, does not aim to add to any of this, but instead to
create a single tool that can be used to use the different themes that are
available.

Thema is a single bash script, which can be executed entirely in a single line,
no need to download or clone anything. The collection of themes, and application
configurations that are stored in this repository define the themes, variants
and outputs that Thema can produce. The script, attempts to detect which
programs are currently installed/configured on your system, and then it injects
the theme configuration into the programs configuration, or files. Then after
all configurations have been updated, a set of commands are executed, to apply
the updates to the system.

## Usage

To use Thema, simply run
```console
foo@bar:~$ curl https://raw.githubusercontent.com/LuxAter/Thema/master/thema | bash -s -- --help
System wide theme configuration tool
Usage: ./thema [-h|--help] [-v|--version] [-o|--output <arg>] [-t|--theme <arg>] [--variant <arg>] [--(no-)list-themes] [--(no-)list-variants] [--(no-)list-outputs] [-q|--(no-)quiet] [-f|--(no-)fancy] [-u|--remote_url <arg>] [-r|--(no-)remote]
	-h, --help: Prints help
	-v, --version: Prints version
	-o, --output: outputs to install new theme (empty by default)
	-t, --theme: theme to install (no default)
	--variant: theme variant to install (no default)
	--list-themes, --no-list-themes: list available themes (off by default)
	--list-variants, --no-list-variants: list available variants (off by default)
	--list-outputs, --no-list-outputs: list available outputs (off by default)
	-q, --quiet, --no-quiet: quiet execution, no output to stdout (off by default)
	-f, --fancy, --no-fancy: fancy formatted output (on by default)
	-u, --remote_url: remote url to use if necessary (default: 'https://raw.githubusercontent.com/LuxAter/Thema/master/')
	-r, --remote, --no-remote: use remote configuration/files (off by default)
```

## Contributing

Contributions are what make the open source community such an amazing place to
be, learn, inspire, and create. Any contributions you make are **greatly
appreciated**.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/<my-feature>`)
3. Commit your changes (`git commit -m '<my-commit-message>'`)
4. Push to the branch (`git push origin feature/<my-feature>`)
5. Open a pull request

The specification for the outputs is still under development, but as of writting
this it is:
```yaml
<name>:
  <source_file>:
    destination:
      - <destination_file>
      - [alternative_destination_file]
    start_of_file: [true|false]
    comment: [<comment_start> <comment_end>]
  [command]:
    - <command_to_run>
    - [additional_command_to_run]
```
Variables of the form `<xxx>` are required and must be set. Variables of the
from `[xxx]` are optional, and can be omited. Notice, that if the `command`
section is defined, then the `command_to_run` is required, but otherwise, they
are optional.

## License

Distributed under the GNU GPLv3 license. See
[`LICENSE.md`](https://github.com/LuxAter/Thema/blob/master/LICENSE.md)
for more information.
