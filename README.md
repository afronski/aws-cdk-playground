# `aws-cdk-playground`

## Motivation

*AWS Cloud Development Kit* is an *open source software* development framework to model and provision your cloud application resources using familiar programming languages.

This repository is a set of examples that we have collected and battle-tested during our work for various clients and project domains. Based on those experiences, @afronski created a talk titled *AWS CDK: Your Infrastructure is Code!* about that we finally arrive to a point when there is no longer need for creating a ton of *YAML* files or code in *DSL* that are immitating real programming languages.

## Examples

- [01-serverless](./01-serverless) - very simple example in *Python* flavor of *AWS CDK* that covers *IaC* for simple serverless application with *API Gateway* and *Lambda* handler in *Python 3.7*.
- [02-constructs](./02-constructs) - more advanced example in *Python* flavor of *AWS CDK* that covers *IaC* for a workshop and generating multiple resources in a loop, creating a custom construct, using various helpers and parametrization via context. This example includes very simple tests as a *sneak peek* for the next example.
- [03-testing](./03-testing) - this time we switch to *TypeScript* to show how easy is to test *IaC* created with *AWS CDK* with use of *Jest* and *aws-cdk-assert* libraries.

- [04-existing-cloudformation-template](./04-existing-cloudformation-template) - last, but not least - an example showing two ways how you can migrate an existing template to the *AWS CDK* (*including a template* and *overrides*).

## Schedule

Repository is a foundation for the lectures - I have performed it in following places:

- [4Developers - Cracow](https://4developers.org.pl/lecture_krakow_2019/#id=55314) (*Cracow*, *Poland*).
- [4Developers - Katowice](https://4developers.org.pl/lecture_katowice_2019/#id=55597) (*Cracow*, *Poland*).

## Prequisites

- `node >= 9.11.2`
- `python >= 3.7.2`
- `npm install -g aws-cdk`
  - `cdk >= 1.9.0`

## License

- [MIT](LICENSE.md)

## Authors

We are [Pattern Match](https://pattern-match.com) - in case of any questions, you can drop us a line over [email](mailto:contact@pattern-match.com).
