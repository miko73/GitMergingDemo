Set synatax to Bourne Again Shell (bash)

export PATH=/ws/gn/ninjatracing:/ws/gn/out:.:$PATH
export PATH=/ws/gn/depot_tools:/ws/gn/ninjatracing:/ws/gn/out:.:$PATH

https://docs.google.com/presentation/d/15Zwb53JcncHfEwHpnG_PoIbbzQ3GQi_cpujYwbpcbZo/htmlpresent

https://jpospisil.com/2014/03/16/replacing-make-with-ninja.html

/*========================================================================*/


root@e9e3d530133b:/ws/gn/examples/simple_build# gn help

Commands (type "gn help <command>" for more help):
  analyze: Analyze which targets are affected by a list of files.
  args: Display or configure arguments declared by the build.
  check: Check header dependencies.
  clean: Cleans the output directory.
  clean_stale: Cleans the stale output files from the output directory.
  desc: Show lots of insightful information about a target or config.
  format: Format .gn files.
  gen: Generate ninja files.
  help: Does what you think.
  ls: List matching targets.
  meta: List target metadata collection results.
  outputs: Which files a source/target make.
  path: Find paths between two targets.
  refs: Find stuff referencing a target or file.

Target declarations (type "gn help <function>" for more help):
  action: Declare a target that runs a script a single time.
  action_foreach: Declare a target that runs a script over a set of files.
  bundle_data: [iOS/macOS] Declare a target without output.
  copy: Declare a target that copies files.
  create_bundle: [iOS/macOS] Build an iOS or macOS bundle.
  executable: Declare an executable target.
  generated_file: Declare a generated_file target.
  group: Declare a named group of targets.
  loadable_module: Declare a loadable module target.
  rust_library: Declare a Rust library target.
  rust_proc_macro: Declare a Rust procedural macro target.
  shared_library: Declare a shared library target.
  source_set: Declare a source set target.
  static_library: Declare a static library target.
  target: Declare an target with the given programmatic type.

Buildfile functions (type "gn help <function>" for more help):
  assert: Assert an expression is true at generation time.
  config: Defines a configuration object.
  declare_args: Declare build arguments.
  defined: Returns whether an identifier is defined.
  exec_script: Synchronously run a script and return the output.
  filter_exclude: Remove values that match a set of patterns.
  filter_include: Remove values that do not match a set of patterns.
  foreach: Iterate over a list.
  forward_variables_from: Copies variables from a different scope.
  get_label_info: Get an attribute from a targets label.
  get_path_info: Extract parts of a file or directory name.
  get_target_outputs: [file list] Get the list of outputs from a target.
  getenv: Get an environment variable.
  import: Import a file into the current scope.
  not_needed: Mark variables from scope as not needed.
  pool: Defines a pool object.
  print: Prints to the console.
  process_file_template: Do template expansion over a list of files.
  read_file: Read a file into a variable.
  rebase_path: Rebase a file or directory to another location.
  set_default_toolchain: Sets the default toolchain name.
  set_defaults: Set default values for a target type.
  set_sources_assignment_filter: Deprecated feature.
  split_list: Splits a list into N different sub-lists.
  string_join: Concatenates a list of strings with a separator.
  string_replace: Replaces substring in the given string.
  string_split: Split string into a list of strings.
  template: Define a template rule.
  tool: Specify arguments to a toolchain tool.
  toolchain: Defines a toolchain.
  write_file: Write a file to disk.

Built-in predefined variables (type "gn help <variable>" for more help):
  current_cpu: [string] The processor architecture of the current toolchain.
  current_os: [string] The operating system of the current toolchain.
  current_toolchain: [string] Label of the current toolchain.
  default_toolchain: [string] Label of the default toolchain.
  gn_version: [number] The version of gn.
  host_cpu: [string] The processor architecture that GN is running on.
  host_os: [string] The operating system that GN is running on.
  invoker: [string] The invoking scope inside a template.
  python_path: [string] Absolute path of Python.
  root_build_dir: [string] Directory where build commands are run.
  root_gen_dir: [string] Directory for the toolchain's generated files.
  root_out_dir: [string] Root directory for toolchain output files.
  target_cpu: [string] The desired cpu architecture for the build.
  target_gen_dir: [string] Directory for a target's generated files.
  target_name: [string] The name of the current target.
  target_os: [string] The desired operating system for the build.
  target_out_dir: [string] Directory for target output files.

Variables you set in targets (type "gn help <variable>" for more help):
  aliased_deps: [scope] Set of crate-dependency pairs.
  all_dependent_configs: [label list] Configs to be forced on dependents.
  allow_circular_includes_from: [label list] Permit includes from deps.
  arflags: [string list] Arguments passed to static_library archiver.
  args: [string list] Arguments passed to an action.
  asmflags: [string list] Flags passed to the assembler.
  assert_no_deps: [label pattern list] Ensure no deps on these targets.
  bridge_header: [string] Path to C/Objective-C compatibility header.
  bundle_contents_dir: Expansion of {{bundle_contents_dir}} in create_bundle.
  bundle_deps_filter: [label list] A list of labels that are filtered out.
  bundle_executable_dir: Expansion of {{bundle_executable_dir}} in create_bundle
  bundle_resources_dir: Expansion of {{bundle_resources_dir}} in create_bundle.
  bundle_root_dir: Expansion of {{bundle_root_dir}} in create_bundle.
  cflags: [string list] Flags passed to all C compiler variants.
  cflags_c: [string list] Flags passed to the C compiler.
  cflags_cc: [string list] Flags passed to the C++ compiler.
  cflags_objc: [string list] Flags passed to the Objective C compiler.
  cflags_objcc: [string list] Flags passed to the Objective C++ compiler.
  check_includes: [boolean] Controls whether a targets files are checked.
  code_signing_args: [string list] Arguments passed to code signing script.
  code_signing_outputs: [file list] Output files for code signing step.
  code_signing_script: [file name] Script for code signing.
  code_signing_sources: [file list] Sources for code signing step.
  complete_static_lib: [boolean] Links all deps into a static library.
  configs: [label list] Configs applying to this target or config.
  contents: Contents to write to file.
  crate_name: [string] The name for the compiled crate.
  crate_root: [string] The root source file for a binary or library.
  crate_type: [string] The type of linkage to use on a shared_library.
  data: [file list] Runtime data file dependencies.
  data_deps: [label list] Non-linked dependencies.
  data_keys: [string list] Keys from which to collect metadata.
  defines: [string list] C preprocessor defines.
  depfile: [string] File name for input dependencies for actions.
  deps: [label list] Private linked dependencies.
  externs: [scope] Set of Rust crate-dependency pairs.
  framework_dirs: [directory list] Additional framework search directories.
  frameworks: [name list] Name of frameworks that must be linked.
  friend: [label pattern list] Allow targets to include private headers.
  include_dirs: [directory list] Additional include directories.
  inputs: [file list] Additional compile-time dependencies.
  ldflags: [string list] Flags passed to the linker.
  lib_dirs: [directory list] Additional library directories.
  libs: [string list] Additional libraries to link.
  metadata: [scope] Metadata of this target.
  module_name: [string] The name for the compiled module.
  output_conversion: Data format for generated_file targets.
  output_dir: [directory] Directory to put output file in.
  output_extension: [string] Value to use for the output's file extension.
  output_name: [string] Name for the output file other than the default.
  output_prefix_override: [boolean] Don't use prefix for output name.
  outputs: [file list] Output files for actions and copy targets.
  partial_info_plist: [filename] Path plist from asset catalog compiler.
  pool: [string] Label of the pool used by the action.
  precompiled_header: [string] Header file to precompile.
  precompiled_header_type: [string] "gcc" or "msvc".
  precompiled_source: [file name] Source file to precompile.
  product_type: [string] Product type for Xcode projects.
  public: [file list] Declare public header files for a target.
  public_configs: [label list] Configs applied to dependents.
  public_deps: [label list] Declare public dependencies.
  rebase: [boolean] Rebase collected metadata as files.
  response_file_contents: [string list] Contents of .rsp file for actions.
  script: [file name] Script file for actions.
  sources: [file list] Source files for a target.
  swiftflags: [string list] Flags passed to the swift compiler.
  testonly: [boolean] Declares a target must only be used for testing.
  visibility: [label list] A list of labels that can depend on a target.
  walk_keys: [string list] Key(s) for managing the metadata collection walk.
  weak_frameworks: [name list] Name of frameworks that must be weak linked.
  write_runtime_deps: Writes the targets runtime_deps to the given path.
  xcasset_compiler_flags: [string list] Flags passed to xcassets compiler
  xcode_extra_attributes: [scope] Extra attributes for Xcode projects.
  xcode_test_application_name: [string] Name for Xcode test target.

Other help topics:
  all: Print all the help at once
  buildargs: How build arguments work.
  dotfile: Info about the toplevel .gn file.
  execution: Build graph and execution overview.
  grammar: Language and grammar for GN build files.
  input_conversion: Processing input from exec_script and read_file.
  file_pattern: Matching more than one file.
  label_pattern: Matching more than one label.
  labels: About labels.
  metadata_collection: About metadata and its collection.
  ninja_rules: How Ninja build rules are named.
  nogncheck: Annotating includes for checking.
  output_conversion: Specifies how to transform a value to output.
  runtime_deps: How runtime dependency computation works.
  source_expansion: Map sources to outputs for scripts.
  switches: Show available command-line switches.
root@e9e3d530133b:/ws/gn/examples/simple_build#

o
/*========================================================================*/
/*========================================================================*/
root@1923fc09e643:/ws# git clone https://gn.googlesource.com/gn
Cloning into 'gn'...
remote: Sending approximately 29.93 MiB ...
remote: Counting objects: 1, done
remote: Total 30360 (delta 16166), reused 30360 (delta 16166)
Receiving objects: 100% (30360/30360), 29.93 MiB | 7.25 MiB/s, done.
Resolving deltas: 100% (16166/16166), done.
root@1923fc09e643:/ws# cd gn
export PATH=$PATH:/ws/Python-3.9.1

python build/gen.py
ninja -C out # make ./out directory and make all *.o files form cc and h files.
# log file stored in ./out/.ninja_log
# root@e9e3d530133b:/ws/gn# ninjatracing ./out/.ninja_log > ./trace.json
# root@e9e3d530133b:/ws/gn# view ./trace.json
# root@e9e3d530133b:/ws/gn#


root@1923fc09e643:/ws/gn/examples/simple_build# ./gn_unittests
root@1923fc09e643:/ws/gn/examples/simple_build# cd ../examples/
root@1923fc09e643:/ws/gn/examples/simple_build# cd simple_build/
root@1923fc09e643:/ws/gn/examples/simple_build# ../../out/gn gen out/default
# creates
|-- out
|   `-- default
|       |-- args.gn
|       |-- build.ninja
|       |-- build.ninja.d
|       |-- obj
|       |   |-- hello.ninja
|       |   |-- hello_shared.ninja
|       |   `-- hello_static.ninja
|       `-- toolchain.ninja

root@1923fc09e643:/ws/gn/examples/simple_build# ../../out/gn args --list out/default
current_cpu
    Current value (from the default) = ""
      (Internally set; try `gn help current_cpu`.)

current_os
    Current value (from the default) = ""
      (Internally set; try `gn help current_os`.)

host_cpu
    Current value (from the default) = "x64"
      (Internally set; try `gn help host_cpu`.)

host_os
    Current value (from the default) = "linux"
      (Internally set; try `gn help host_os`.)

target_cpu
    Current value (from the default) = ""
      (Internally set; try `gn help target_cpu`.)

target_os
    Current value (from the default) = ""
      (Internally set; try `gn help target_os`.)


root@1923fc09e643:/ws/gn/examples/simple_build# ninja -C out/default
ninja: Entering directory `out/default
[6/6] LINK hello



root@e9e3d530133b:/ws/gn/examples/simple_build# ninja -C out/default
ninja: Entering directory `out/default
[6/6] LINK hello

is generated in /ws/gn/examples/simple_build/out/default

root@e9e3d530133b:/ws/gn/examples/simple_build# tree
|-- out
|   `-- default
|       |-- hello
|       |-- libhello_shared.so
|       |-- obj
|       |   |-- hello.hello.o
|       |   |-- libhello_shared.hello_shared.o
|       |   |-- libhello_static.a
|       |   `-- libhello_static.hello_static.o




root@e9e3d530133b:/ws/gn/examples/simple_build# cat BUILD.gn
# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

executable("hello") {
  sources = [ "hello.cc" ]

  deps = [
    ":hello_shared",
    ":hello_static",
  ]
}

shared_library("hello_shared") {
  sources = [
    "hello_shared.cc",
    "hello_shared.h",
  ]

  defines = [ "HELLO_SHARED_IMPLEMENTATION" ]
}

static_library("hello_static") {
  sources = [
    "hello_static.cc",
    "hello_static.h",
  ]
}

miko build
command

gn gen out/default
  creates
  |-- out
  |   -- default
  |       |-- obj
  |       |   |-- hello.ninja
  |       |   |-- hello_shared.ninja
  |       |   |-- hello_static.ninja





root@e9e3d530133b:/ws/gn/examples/simple_build/tutorial# gn analyze gen out
Done. Made 3 targets from 4 files in 6ms

root@e9e3d530133b:/ws/gn/examples/simple_build/tutorial# cat BUILD.gn
executable("tutorial") {
  sources = [
    "tutorial.cc",
  ]
}
group("tools") {
  deps = [
    # This will expand to the name "//tutorial:tutorial" which is the full name
    # of our new target. Run "gn help labels" for more.
    "//tutorial",
  ]
}

/*========================================================================*/
root@e9e3d530133b:/ws/gn/examples/simple_build# cd ../../..
root@e9e3d530133b:/ws# cd gn
root@e9e3d530133b:/ws/gn# git clone https://github.com/nico/ninjatracing;
Cloning into 'ninjatracing'...
remote: Enumerating objects: 126, done.
remote: Total 126 (delta 0), reused 0 (delta 0), pack-reused 126
Receiving objects: 100% (126/126), 33.15 KiB | 465.00 KiB/s, done.
Resolving deltas: 100% (57/57), done.



/*========================================================================*/
file authorized_keys has to be preserved to be able to access host

debian@miko-debian-dev:~/.ssh$ ls -l
total 12
-rw------- 1 debian debian  754 Feb  9 13:25 authorized_keys
/*===============================================================================================*/

 apt install -y build-essential g++ unzip ninja-build pkg-config libreadline-dev

GN final install

sudo apt-get install ninja-build
cd gn
ninja -C out 
sudo apt-get install build-essential clang
ninja -C out 

export PATH=/home/debian/gn/out:/home/debian/sluha:.:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/gamesG



http://neugierig.org/software/chromium/notes/2011/02/ninja.html
export PATH=/home/debian/gn/out:/home/debian/sluha:.:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
