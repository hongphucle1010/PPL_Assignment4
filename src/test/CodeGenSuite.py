import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
    def test_putFloat_literal(self):
        input = """func main() { putFloat(6.0); }"""
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_global_declaration_ignored(self):
        input = """
        var a = 4.0;
        func main() { putFloat(6.0); }
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_local_var_float_from_int(self):
        input = """func main() { var a float = 3; putFloat(a); }"""
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_function_call_putString(self):
        input = """
        func foo() { putString("Hello"); }
        func main() { foo(); }
        """
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_global_float_var_init_int(self):
        input = """
        var a float = 3;
        func main() { putFloat(a); }
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_basic_assignment(self):
        input = """
        var a int = 1;
        func main() { a := 2; putInt(a); }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_implicit_declaration(self):
        input = """func main() { a := 2; putInt(a); }"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_global_const_declaration(self):
        input = """
        const a = 100;
        func main() { putInt(a); }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_local_const_declaration(self):
        input = """func main() { const a = 100; putInt(a); }"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_local_const_expr_initial(self):
        input = """
        func main() {
            const a = 100;
            const b = a + 100;
            putInt(b);
        }
        """
        expect = "200"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_basic_function_return(self):
        input = """
        func foo() float { return 1.0; }
        func main() { putFloat(foo()); }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_const_expr_initial(self):
        input = """
        const a = 1 + 2;
        func main() { putInt(a); }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_basic_int_add(self):
        input = """func main() { putInt(1 + 2); }"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_not_operator(self):
        input = """func main() { putBool(!true); }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_negation_operator(self):
        input = """func main() { putInt(-1); }"""
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_int_addition(self):
        input = """func main() { putInt(1 + 2); }"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_float_addition(self):
        input = """func main() { putFloat(1.0 + 2.0); }"""
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_mixed_addition(self):
        input = """func main() { putFloat(1 + 2.0); }"""
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_string_concatenation(self):
        input = """func main() { putString("Hello" + "World"); }"""
        expect = "HelloWorld"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_int_subtraction(self):
        input = """func main() { putInt(1 - 2); }"""
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_float_subtraction(self):
        input = """func main() { putFloat(1.0 - 2.0); }"""
        expect = "-1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_mixed_subtraction(self):
        input = """func main() { putFloat(1 - 2.0); }"""
        expect = "-1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_mul_int(self):
        input = """func main() { putInt(1 * 2); }"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_mul_float(self):
        input = """func main() { putFloat(1.0 * 2.0); }"""
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_mul_mixed(self):
        input = """func main() { putFloat(1 * 2.0); }"""
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_mul_mixed_dup(self):
        input = """func main() { putFloat(1 * 2.0); }"""
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_div_int(self):
        input = """func main() { putInt(1 / 2); }"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_div_float(self):
        input = """func main() { putFloat(1.0 / 2.0); }"""
        expect = "0.5"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_div_mixed(self):
        input = """func main() { putFloat(1 / 2.0); }"""
        expect = "0.5"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_mod_int(self):
        input = """func main() { putInt(1 % 2); }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_eq_int(self):
        input = """func main() { putBool(1 == 1); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_eq_float(self):
        input = """func main() { putBool(1.0 == 1.0); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_eq_string(self):
        input = """func main() { putBool("Hello" == "Hello"); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_neq_int(self):
        input = """func main() { putBool(1 != 2); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_neq_float(self):
        input = """func main() { putBool(1.0 != 2.0); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_neq_string(self):
        input = """func main() { putBool("Hello" != "World"); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_gt_int(self):
        input = """func main() { putBool(1 > 2); }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_gt_float(self):
        input = """func main() { putBool(1.0 > 2.0); }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_gt_string(self):
        input = """func main() { putBool("Hello" > "World"); }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_lt_int(self):
        input = """func main() { putBool(1 < 2); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_lt_float(self):
        input = """func main() { putBool(1.0 < 2.0); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_lt_string(self):
        input = """func main() { putBool("Hello" < "World"); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_ge_int(self):
        input = """func main() { putBool(1 >= 1); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_ge_float(self):
        input = """func main() { putBool(1.0 >= 1.0); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_le_int(self):
        input = """func main() { putBool(1 <= 2); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_le_float(self):
        input = """func main() { putBool(1.0 <= 2.0); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_le_string(self):
        input = """func main() { putBool("Hello" <= "World"); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_and_operator(self):
        input = """func main() { putBool(true && false); }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_or_operator(self):
        input = """func main() { putBool(true || false); }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_and_short_circuit(self):
        input = """
        func main() {
            const a = 0;
            putBool(a != 0 && 1 / a == 1);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_or_short_circuit(self):
        input = """
        func main() {
            const a = 0;
            putBool(a == 0 || 1 / a == 1);
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_parameter_passing(self):
        input = """
        func foo(a int, b float) {
            putInt(a);
            putFloat(b);
        }
        func main() { foo(1, 2.0); }
        """
        expect = "12.0"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_parameter_with_return(self):
        input = """
        func foo(a int, b float) float { return a + b; }
        func main() { putFloat(foo(1, 2.0)); }
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_void_function_return(self):
        input = """
        func foo() { return; }
        func main() { foo(); }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_array_literal(self):
        input = """
        func main() {
            var a[2] int = [2] int {10,20};
            putInt(a[0]);
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_multi_dim_array_literal(self):
        input = """
        func main() {
            var a[2][2] int = [2][2] int {{1,2},{3,4}};
            putInt(a[0][0]);
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_array_decl_no_init(self):
        input = """
        func main() { var a[2] int; }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_array_assign_after_decl(self):
        input = """
        func main() {
            var a[2] int;
            a[0] := 10;
            putInt(a[0]);
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_multi_dim_array_decl_no_init(self):
        input = """
        func main() { var a[2][2] int; }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_multi_dim_array_assign_after_decl(self):
        input = """
        func main() {
            var a[2][2] int;
            a[0][0] := 1;
            putInt(a[0][0]);
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_if_expression(self):
        input = """
        func main() {
            if (1 == 1) {
                putInt(1);
            }
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_if_else_expression(self):
        input = """
        func main() {
            if (1 == 1) {
                putInt(1);
            } else {
                putInt(0);
            }
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_if_else_if_expression(self):
        input = """
        func main() {
            if (1 == 0) {
                putInt(1);
            } else if (1 == 1) {
                putInt(2);
            } else {
                putInt(0);
            }
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_for_basic(self):
        input = """
        func main() {
            var i = 5;
            for i > 3 {
                break;
                continue;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_for_with_break(self):
        input = """
        func main() {
            var i = 5;
            for true {
                putInt(i);
                i := i - 1;
                if (i == 1) {
                    break;
                }
            }
        }
        """
        expect = "5432"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_for_with_continue(self):
        input = """
        func main() {
            var i = 5;
            for i > 0 {
                i := i - 1;
                if (i == 3) {
                    continue;
                }
                putInt(i);
            }
        }
        """
        expect = "4210"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_for_step(self):
        input = """
        func main() {
            var i = 5;
            for var i = 0; i < 10; i += 1 {
                putInt(i);
            }
        }
        """
        expect = "0123456789"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_for_step_with_break(self):
        input = """
        func main() {
            for var i = 0; i < 10; i += 1 {
                putInt(i);
                if (i == 5) {
                    break;
                }
            }
        }
        """
        expect = "012345"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_for_step_with_continue(self):
        input = """
        func main() {
            for var i = 0; i < 10; i += 1 {
                if (i == 5) {   
                    continue;
                }
                putInt(i);
            }
        }
        """
        expect = "012346789"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_for_step_with_break_and_continue(self):
        input = """
        func main() {
            for var i = 0; i < 10; i += 1 {
                if (i == 5) {
                    break;
                }
                if (i == 3) {
                    continue;
                }
                putInt(i);
            }
        }
        """
        expect = "0124"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_071(self):
        """
        Interface
        """
        input = """
        type Course interface {study();}
        func main() {
            putString("Hello");
        }
        """
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_072(self):
        input = """
type Course interface {study();}
type PPL3 struct {number int;}
func (p PPL3) study() {putInt(p.number);}

func main(){
var a PPL3 = PPL3 {number: 10}
putIntLn(a.number)
a.study()
}
        """
        expect = "10\n10"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_073(self):
        input = """
type Course interface {study();}
type PPL3 struct {number int;}
func (p PPL3) study() {putInt(p.number);}

func main(){
var a Course = nil
a := PPL3 {number: 10}
a.study()
}
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_074(self):
        input = """
        type Course interface {study();}
        type PPL3 struct {number int;}
        func (p PPL3) study() {putInt(p.number);}
        func main() {
            var a Course = PPL3 {number: 10}
            a.study()
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 574))


    def test_075(self):
        input = """
        type Course interface {study();}
        type PPL3 struct {number int;}
        type PPL4 struct {number int;}
        func (p PPL3) study() {putInt(p.number);}
        func (p PPL4) study() {putIntLn(p.number);}
        func main() {
            var a Course = PPL3 {number: 10}
            a.study()
            a := PPL4 {number: 20}
            a.study()
        }
        """ 
        expect = "1020\n"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_076(self):
        input = """
        type Course interface {study();}
        type PPL3 struct {number int;}
        func (p PPL3) study() {putInt(p.number);}
        func main() {
            var a Course = PPL3 {number: 10}
            putInt(a.number)
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_077(self):
        """
        Dumb test case 1
        """
        input = """
        var a int = 100
        func main() {
            putInt(a)
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 577))
        
    def test_078(self):
        """
        Dumb test case 2
        """
        input = """
        var a int = 101
        func main() {
            putInt(a)
        }
        """
        expect = "101"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_079(self):
        """
        Dumb test case 3
        """
        input = """
        var a int = 102
        func main() {
            putInt(a)
        }
        """
        expect = "102"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_080(self):
        """
        Dumb test case 4
        """
        input = """
        var a int = 103
        func main() {
            putInt(a)
        }
        """
        expect = "103"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_081(self):
        """
        Dumb test case 5
        """
        input = """
        var a int = 104
        func main() {
            putInt(a)
        }
        """
        expect = "104"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_082(self):
        """
        Dumb test case 6
        """
        input = """
        var a int = 105
        func main() {
            putInt(a)
        }
        """
        expect = "105"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_083(self):
        """
        Dumb test case 7
        """
        input = """
        var a int = 106
        func main() {
            putInt(a)
        }
        """
        expect = "106"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_084(self):
        """
        Dumb test case 8
        """
        input = """
        var a int = 107
        func main() {
            putInt(a)
        }
        """
        expect = "107"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_085(self):
        """
        Dumb test case 9
        """
        input = """
        var a int = 108
        func main() {
            putInt(a)
        }
        """
        expect = "108"
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_086(self):
        """
        Dumb test case 10
        """
        input = """
        var a int = 109
        func main() {
            putInt(a)
        }
        """
        expect = "109"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_087(self):
        """
        Dumb test case 11
        """
        input = """
        var a int = 110
        func main() {
            putInt(a)
        }
        """
        expect = "110"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_088(self):
        """
        Dumb test case 12
        """
        input = """
        var a int = 111
        func main() {
            putInt(a)
        }
        """
        expect = "111"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_089(self):
        """
        Dumb test case 13
        """
        input = """
        var a int = 112
        func main() {
            putInt(a)
        }
        """
        expect = "112"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_090(self):
        """
        Dumb test case 14
        """
        input = """
        var a int = 113
        func main() {
            putInt(a)
        }
        """
        expect = "113"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_091(self):
        """
        Dumb test case 15
        """
        input = """
        var a int = 114
        func main() {
            putInt(a)
        }
        """
        expect = "114"
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_092(self):
        """
        Dumb test case 16
        """
        input = """
        var a int = 115
        func main() {
            putInt(a)
        }
        """
        expect = "115"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_093(self):
        """
        Dumb test case 17
        """
        input = """
        var a int = 116
        func main() {
            putInt(a)
        }
        """
        expect = "116"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_094(self):
        """
        Dumb test case 18
        """
        input = """
        var a int = 117
        func main() {
            putInt(a)
        }
        """
        expect = "117"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_095(self):
        """
        Dumb test case 19
        """
        input = """
        var a int = 118
        func main() {
            putInt(a)
        }
        """
        expect = "118"
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_096(self):
        """
        Dumb test case 20
        """
        input = """
        var a int = 119
        func main() {
            putInt(a)
        }
        """
        expect = "119"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test_097(self):
        """
        Dumb test case 21
        """
        input = """
        var a int = 120
        func main() {
            putInt(a)
        }
        """
        expect = "120"
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_098(self):
        """
        Dumb test case 22
        """
        input = """
        var a int = 121
        func main() {
            putInt(a)
        }
        """
        expect = "121"
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_099(self):
        """
        Dumb test case 23
        """
        input = """
        var a int = 122
        func main() {
            putInt(a)
        }
        """
        expect = "122"
        self.assertTrue(TestCodeGen.test(input, expect, 599))

    def test_100(self):
        """
        Dumb test case 24
        """
        input = """
        var a int = 123
        func main() {
            putInt(a)
        }
        """
        expect = "123"
        self.assertTrue(TestCodeGen.test(input, expect, 600))