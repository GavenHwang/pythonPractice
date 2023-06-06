# -*- coding:utf-8 -*-
from string import Template

from ruamel import yaml


def process_scalar(self):
    if self.analysis is None:
        self.analysis = self.analyze_scalar(self.event.value)
    if self.style is None:
        self.style = self.choose_scalar_style()
    split = not self.simple_key_context
    # if self.analysis.multiline and split    \
    #         and (not self.style or self.style in '\'\"'):
    #     self.write_indent()
    # nprint('xx', self.sequence_context, self.flow_level)
    if self.sequence_context and not self.flow_level:
        self.write_indent()
    if self.style == '"':
        self.write_double_quoted(self.analysis.scalar, split)
    elif self.style == "'":
        self.write_single_quoted(self.analysis.scalar, split)
    elif self.style == '>':
        self.write_folded(self.analysis.scalar)
        if (
                self.event.comment
                and self.event.comment[0]
                and self.event.comment[0].column >= self.indent
        ):
            # comment following a folded scalar must dedent (issue 376)
            self.event.comment[0].column = self.indent - 1  # type: ignore
    elif self.style == '|':
        # self.write_literal(self.analysis.scalar, self.event.comment)
        try:
            cmx = self.event.comment[1][0]
        except (IndexError, TypeError):
            cmx = ""
        self.write_literal(self.analysis.scalar, cmx)
        if (
                self.event.comment
                and self.event.comment[0]
                and self.event.comment[0].column >= self.indent
        ):
            # comment following a literal scalar must dedent (issue 376)
            self.event.comment[0].column = self.indent - 1  # type: ignore
    else:
        self.write_plain(self.analysis.scalar, split)
    self.analysis = None
    self.style = None
    if self.event.comment:
        self.write_post_comment(self.event)


dumper = yaml.RoundTripDumper
# dumper.process_scalar = process_scalar


def yaml_load(yaml_file):
    with open(yaml_file, "r", encoding="utf-8") as fr:
        result = yaml.safe_load(fr.read())
    return result


def yaml_dump(dict_or_str):
    return yaml.dump(dict_or_str, Dumper=dumper, allow_unicode=True)


result = yaml_load("result.yaml")
result["my_replace"] = "${name}"
print(result)
print("---------------")
result_str = yaml_dump(result)
print(result_str)
print("---------------")
tem = Template(yaml_dump(result_str))
result_str_replace = tem.safe_substitute({"name": "2022-12-15 12:00:00"})
print(yaml.safe_load(result_str_replace))
