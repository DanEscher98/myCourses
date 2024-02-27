# DEVLOG

## Machine info
```
$ cat /etc/os-release
VERSION="38 (Workstation Edition)"
ID=fedora

$ clang --version
clang version 16.0.6 (Fedora 16.0.6-3.fc38)
Target: x86_64-redhat-linux-gnu

$ gcc --version
gcc (GCC) 13.2.1 20231011 (Red Hat 13.2.1-4)
```


## Notes

- While `v1.1.0` successfully compiles using `cargo build --release`, it
  encounters linker errors (with default `cc`) when running `cargo test
  --release`. Changing linker to `rust-ld` at `.cargo/config.toml` didn't fix
  it.

```toml
[dependencies]
gstd = "1.1.0"
gtest = "1.1.0" # fails running `cargo test --release`
...
```

- It is safe to use dependencies from `gstd` at revision `175f69b7`, versions
  from `v1.0.1` to `v1.0.5` are ok. This has been validated using the toolchain
  `nightly-2023-10-10` (`rustc 1.75`). Prior to revision `175f69b7`, issues
  arose due to:
    - unknown `feature(panic_oom_payload)` in `gstd/src/lib.rs:130`
    - invalid `use alloc::alloc::AllocErrorPanicPayload` in
      `/gstd/src/common/handlers.rs:29`.

  Currently, all templates downloaded using `gear gcli new
  --template=$template` (gear-gcli 1.1.0) specify `gstd = { rev="946ac47" }`,
  which fails to compile, adding frictions for newcomers.

```toml
# Cargo.toml
[dependencies]
gstd = { git = "https://github.com/gear-tech/gear.git", rev = "175f69b7" }
# gstd = { git = "https://github.com/gear-tech/gear.git", tag = "v1.0.2" } # also works

# rust-toolchain.toml
[toolchain]
channel = "nightly-2023-10-10"
```


- Ensure that the dependency `gear-wasm-builder` is specified under
  `[build-dependencies]`. Avoid setting the `wasm-opt` feature in the
  `gear-wasm-builder` dependency because it leads to multiple compilation
  errors. It has been verified that the optimization is performed without the
  `wasm-opt` feature since `^1.0.1`.


## Minimal working configuration

### Cargo.toml

```toml
[package]
name = "hello-world"
version.workspace = true
edition.workspace = true

[dependencies]
gstd = { workspace = true, features = ["debug"] }
gmeta.workspace = true
gmeta.workspace = true

[dev-dependencies]
gstd = { workspace = true, features = ["debug"] }
gtest.workspace = true
gclient.workspace = true

[workspace.package]
version = "0.1.0"
edition = "2021"

[workspace.dependencies]
gstd = { git = "https://github.com/gear-tech/gear.git", tag = "v1.0.5" }
gclient = { git = "https://github.com/gear-tech/gear.git", tag = "v1.0.5" }
gmeta = { git = "https://github.com/gear-tech/gear.git", tag = "v1.0.5" }
gtest = { git = "https://github.com/gear-tech/gear.git", tag = "v1.0.5" }
gear-wasm-builder = { git = "https://github.com/gear-tech/gear.git", tag = "v1.0.5" }

[features]
binary-vendor = []
```


### rust-toolchain.toml

```toml
[toolchain]
channel = "nightly-2023-10-10"
targets = ["wasm32-unknown-unknown"]
profile = "minimal"
components = ["rustfmt", "clippy"]
```
