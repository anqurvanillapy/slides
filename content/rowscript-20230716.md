# 你能从依赖类型版 JS 中获得什么

[Anqur] @ [∞-type Café 暑校 '23]

[Anqur]: https://github.com/anqurvanillapy
[∞-type Café 暑校 '23]: https://infinity-type-cafe.github.io/ntype-cafe-summer-school/

--

⚠️ 如果你看到这行字, 说明演讲还没发生, 不要往下看啦~

--

## Hi folks

* 社畜一枚, 白天大道至简 <!-- .element: class="fragment" -->
* 晚上写写 PL 玩具 <!-- .element: class="fragment" -->
* 18 年认识 ice1k 开始走上 PL 不归路 <!-- .element: class="fragment" -->

--

## 今天讲什么

* 带货 <!-- .element: class="fragment" -->
* 工业人的 PL 心路历程 <!-- .element: class="fragment" -->
* 如何迭代自己的通用语言 <!-- .element: class="fragment" -->
* 心灵鸡汤 <!-- .element: class="fragment" -->

---

## 🫳🔨🧙🔮

你会创造怎样的语言?

--

## 魔改 C 语言

* 存储, Linux, 内核模块 <!-- .element: class="fragment" -->
* 内存与资源管理 <!-- .element: class="fragment" -->
* Python 家族语法 <!-- .element: class="fragment" -->

--

## Cyrup

C with much sugar 🍬

--

## 基于 DT 扩展

* "群里人人都会手写 DT 🤦"
* 怎么写, 晚上游客 (Guest0x0) 会教 <!-- .element: class="fragment" -->
* 坚持下, 我等下也会教 :) <!-- .element: class="fragment" -->

--

## 资源管理: QTT

* Quantitative types
  * [The Syntax and Semantics of Quantitative Types], Bob Atkey, 2018
* 函数参数 modal: 0, 1, n
  * 0: 不能在函数体内引用, 可用于类型
  * 1: 只能引用一次
  * n: 随意引用

[The Syntax and Semantics of Quantitative Types]: https://bentnib.org/quantitative-type-theory.html

--

## 🍬

<img src="./content/assets/qtt-tweet.png" alt="cyrup-qtt" width="50%">

--

## 🕌👖🌶️

* `rid` 表示 0
* `mut` 表示 1
* 默认为 n

--

<img src="./content/assets/cyrup-qtt.png" alt="cyrup-qtt" width="60%">

--

## Trivia

实际上 QTT 就是 [Idris 2] 的核心.

[Idris 2]: https://idris2.readthedocs.io/en/latest/tutorial/multiplicities.html

--

## Transpile

* 编译后吐出 ANSI C 源码
* 依赖系统携带的 clang/gcc 编译
* 俺不懂 LLVM 😁
* 还存在于想象, 没做完

--

## 面对命中注定的失败 😭

* 22 年中停止了 Cyrup 的开发
* 存储项目不 (cai) 做 (yuan) 了 <!-- .element: class="fragment" -->
* 不是人人都要写内核模块 <!-- .element: class="fragment" -->
* 系统编程内卷: Rust, Go, Zig...<!-- .element: class="fragment" -->

---

## 再出发: 从娱乐圈出道

重新思考到底要做什么.

--

## 灵感/经验 1

* ["Total type theory really is adequate for general-purpose programming"], Jon Sterling, WITS '22
* 但江大林举的居然是 Idris 2 和 Lean 4 的例子 😅 <!-- .element: class="fragment" -->
* 工业界还没达成但是应该达成这个共识 <!-- .element: class="fragment" -->

["Total type theory really is adequate for general-purpose programming"]: https://youtu.be/lqBFq7aRReY?t=2296

--

## Why DT tho?

工业界里各种古老的技术...

* 宏, 过程宏 (卫生宏)
  * 插件和 IDE 直接傻眼 <!-- .element: class="fragment" -->
  * 将 parser 复杂化 <!-- .element: class="fragment" -->
* 基于 DSL/AST/目标代码 的代码生成
  * 依赖构建环境 <!-- .element: class="fragment" -->
  * 生成的代码通常没法引用原始数据 <!-- .element: class="fragment" -->

--

## DT solutions?

* 编译期计算
* 静态反射
  * [GHC.Generics]
  * [Elaborator reflection]

[GHC.Generics]: https://hackage.haskell.org/package/base-4.18.0.0/docs/GHC-Generics.html
[Elaborator reflection]: https://github.com/stefan-hoeck/idris2-elab-util/blob/main/src/Doc/Index.md

--

## 灵感 2

* 从大众更容易接受的语言开始改造
* 什么语言到处都可以运行?

--

## JavaScript

* "... it makes sense to think of JavaScript as the [universal scripting language]", Ryan Dahl, JavaScript Containers
* 只要有界面的设备, 大概率能编写、调试和运行 JavaScript <!-- .element: class="fragment" -->
* 俺不懂 WebAssembly 😄 <!-- .element: class="fragment" -->

[universal scripting language]: https://tinyclouds.org/javascript_containers

--

## 前端也很卷

* TypeScript
* PureScript, Elm
* ReScript, MoonBit
* ...

--

## 但我想要 JS 家族语法 😀

* Parsing 的生态非常的混乱 <!-- .element: class="fragment" -->
  * VSCode 和 GitHub: TextMate <!-- .element: class="fragment" -->
  * IntelliJ: Bison 和 Flex <!-- .element: class="fragment" -->
  * 自己写玩具: "诶小亮给他整个 parsec 儿" <!-- .element: class="fragment" -->
* 降低用户心智 <!-- .element: class="fragment" -->
  * 不过 template 能降低学习成本 <!-- .element: class="fragment" -->
* 沿用各种平台和插件现有的高亮 <!-- .element: class="fragment" -->
* 此处只剩下 TypeScript 符合想法 <!-- .element: class="fragment" -->

--

## TypeScript

* 繁杂的类型体操 <!-- .element: class="fragment" -->
  * 上来甩手写 Church numeral
* Literal type <!-- .element: class="fragment" -->
* Intersection type 不是那么强大 <!-- .element: class="fragment" -->
  * 月经问题: 怎么实现 ADT
* 编译期到底能做多少计算, 不知道 <!-- .element: class="fragment" -->

--

## 灵感 3

"也许使用 row polymorphism 可以模拟 JS 的 prototype-based OOP", [玩火], 某次群聊.

[玩火]: https://github.com/niltok

--

## 所有灵感

* Total type theory: DT
* 流行的语言: JavaScript
* 更好的类型扩展: Row poly, etc.

---

## 试想一下这样的语言

* 依赖类型 <!-- .element: class="fragment" -->
* Object type in JS <!-- .element: class="fragment" -->
* Enum type in Rust <!-- .element: class="fragment" -->
* OOP <!-- .element: class="fragment" -->
* Typeclass in Haskell <!-- .element: class="fragment" -->
* 静态反射 <!-- .element: class="fragment" -->
* 生成 ES6 标准的 JS <!-- .element: class="fragment" -->

--

## 🚣 [RowScript]

* 22 年 11 月项目开始
* Rust 写的编译器
* 刚提到的特性都已经支持了

[RowScript]: https://github.com/rowscript/rowscript

--

## 学术细节: Row poly

* Object 和 enum 是怎么实现的? <!-- .element: class="fragment" -->
  * [Abstracting extensible data types], 2019
  * 又叫做 concatenation-based row polymorphism <!-- .element: class="fragment" -->
  * 和 PureScript, OCaml 的实现完全不同 <!-- .element: class="fragment" -->

[Abstracting extensible data types]: https://dl.acm.org/doi/10.1145/3290325

--

## 其他学术细节

* OOP <!-- .element: class="fragment" -->
  * 基于 virtual table
  * 并不是 ES6 class 的语法糖
  * 而是 row poly 的语法糖 <!-- .element: class="fragment" -->
* Typeclass: 抄的 Haskell <!-- .element: class="fragment" -->

--

## 代码演示

--

## 玩具如何进化

* Theorist, proposer 😋 <!-- .element: class="fragment" -->
* Compiler writer 🙋 <!-- .element: class="fragment" -->
* Library writer 🙅 <!-- .element: class="fragment" -->
* Application writer 😫 <!-- .element: class="fragment" -->

RowScript 能用, 但又不能用 🤣 <!-- .element: class="fragment" -->

--

## "道理我都懂..."

* 如果我也想自己做一款语言, 怎么弄?
* "教教我", "大的要来了" <!-- .element: class="fragment" -->
* 很简单, 抄代码 <!-- .element: class="fragment" -->

---

## 自己造 DT 的前提

* Pi, Sigma <!-- .element: class="fragment" -->
* Holes <!-- .element: class="fragment" -->
* Implicit argument <!-- .element: class="fragment" -->
* Inductive types, etc. <!-- .element: class="fragment" -->

--

## 抄什么代码?

* [ice1000/guest0x0] v0.1: 最基础的 MLTT
  * 需要修复 [一个 bug]
  * 将 Java 翻译成你喜欢的语言, 或直接拿来用
* [ice1000/anqur]: 支持 inductive types

[ice1000/guest0x0]: https://github.com/ice1000/guest0x0/releases/tag/v0.1
[一个 bug]: https://github.com/ice1000/guest0x0/commit/65f0a602da92baa3ccb277589363545ded1fe6d9
[ice1000/anqur]: https://github.com/ice1000/anqur

--

## 要抄多久啊?

* 阿冰的几个玩具实现 MLTT 的 Java 代码量 <!-- .element: class="fragment" -->
* RowScript 最初实现 MLTT 的 Rust 代码量 <!-- .element: class="fragment" -->

🥳🎉 皆 <1K. <!-- .element: class="fragment" -->

--

## "作业"

* 多写测试, 多单步调试
* 需要在抄代码的过程中弄懂的各种概念

--

* Surface syntax
  * Parser: Parse
* Concrete syntax, aka expression, `Expr`
  * Translator: Translate
  * Resolver: Resolve
  * Elaborator: Check, infer, synthesize
* Abstract syntax, aka term, `Term`, (canonical/neutral) value
  * Renamer: Rename (why???)
  * Normalizer: Normalize, normal form, substitution
  * Unifier: Unify, conversion check

--

## Why imperative?

* 为啥不用 Haskell/OCaml 等呢? <!-- .element: class="fragment" -->
* 工业语言往往现有的轮子多 <!-- .element: class="fragment" -->
* 面向工业, 最好用工业语言 <!-- .element: class="fragment" --> ~~(骗取社区信任)~~

--

## Ergonomics

DT 为了用户用得舒服, 并不简单...

* Implicit argument <!-- .element: class="fragment" -->
  * 前提条件是 holes <!-- .element: class="fragment" -->
* Inductive types <!-- .element: class="fragment" -->
  * Dependent pattern matching <!-- .element: class="fragment" -->
  * Overlapping patterns <!-- .element: class="fragment" -->

--

## 啃纸啃代码 🤒️

* 绝世经典 [elaboration-zoo]
* 看 RowScript 实现也行 <!-- .element: class="fragment" -->

[elaboration-zoo]: https://github.com/AndrasKovacs/elaboration-zoo

---

## 心灵鸡汤

--

## Callback: 🔨🔮

* 你想给工业界带来什么? <!-- .element: class="fragment" -->
* "我来自学术界" "我还是学生, 还很迷惑" <!-- .element: class="fragment" -->
  * 实实在在能运行的软件和代码 <!-- .element: class="fragment" -->

--

> 如何看待 MoonBit 编程语言内测? 能给我国编程语言生态带来影响力吗?

[圆角骑士魔理沙的回答] - 知乎

[圆角骑士魔理沙的回答]: https://www.zhihu.com/question/603882336/answer/3055314396

--

> "..., 他们之中的绝大部分人, 都找不到相关的工作, 在毕业以后只能去做跟编程语言毫无关系的工作. PL 对他们来说, 就只是一个奇怪的爱好."

--

这部分人也非常期望能向 *PL 社区*/*工业界* 带来自己的贡献.

Thanks, see ya! 🥰 <!-- .element: class="fragment" -->
