# Modules and packaging decisions

Consult when changing compiler options, imports, package exports or build output. Select documentation for the installed compiler/runtime rather than copying a universal tsconfig.

| Consumer/host | Establish | Verify |
| --- | --- | --- |
| Runtime executes emitted JavaScript | Runtime version, package type, extensions and ESM/CommonJS interoperability | Actual emitted imports and supported entrypoints load outside the development runner |
| Bundler consumes TypeScript | Bundler resolution/transforms, target and runtime globals | Production bundle, split chunks/assets and actual target execution |
| Runtime executes TypeScript directly | Supported syntax/transforms, resolution and whether checking occurs | Separate type check plus direct execution on the promised runtime version |
| Published library | Public entrypoints, module formats, declarations, supported compiler/runtime and peer dependencies | Packed contents and representative external consumer type/runtime checks |
| Workspace/shared package | Ownership, build order, public imports and dependency graph | Consumer works through intended exports rather than accidental source aliases |

A declaration file is a consumer contract, not proof that emitted JavaScript behaves accordingly. Check that exported values exist at runtime, imports resolve and public types do not refer to unpublished paths. A compiler can accept imports which a bundler or runtime rejects. Separate declaration generation, transpilation, bundling and type checking in the actual toolchain.

For large type/build cost, inspect diagnostics and dependency boundaries before adding elaborate project references or disabling checks. A valid type assertion can still misrepresent untrusted data; runtime validation and semantic tests remain necessary.

Primary references: [module theory](https://www.typescriptlang.org/docs/handbook/modules/theory.html), [compiler-option selection](https://www.typescriptlang.org/docs/handbook/modules/guides/choosing-compiler-options.html), [publishing declarations](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html), [Node TypeScript execution](https://nodejs.org/api/typescript.html). Other accepted hosts require their own version-matched documentation.
