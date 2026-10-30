# 来源登记

[catalogue.json](catalogue.json) 列出研究路线中的19个资料区及用途。前八篇专题采用 Refactoring UI 前八个主题组的页面观察；第九篇另含本地PDF指定页阅读启发与六项公开来源的限定文字核验。未列入的资料仍是研究路线，不能据篇数推高阅读完成度。资料区名称不是作者身份，也不是逐项主张的依据。

当前没有把私人课程页面链接或原始媒体定位符复制进公开目录。没有核到的信息保留未知，不根据品牌名补造链接或许可。

[主来源登记](refactoring-ui.json)记录了本次实际核验的官方出版页和作者页面。Refactoring UI 由 Adam Wathan 与 Steve Schoger 共同创作；官方出版页的前八组目录与本次整理页题目可对应。官方网页只支持作者和著作目录的核验，不代表已逐页校勘出版PDF、取得素材再分发许可或验证全部设计主张。[官方出版页](https://refactoringui.com/)、[Steve Schoger 的作者介绍](https://www.steveschoger.com/book/)、[Adam Wathan 的课程介绍](https://adamwathan.me/courses/)。

| 专题登记 | 资料整理页 | 图片引用观察 | 额外技术核验 |
|---|---:|---:|---|
| [从任务开始](starting-from-a-task.json) | 5 | 28 | 无技术规格补引 |
| [层级与操作](hierarchy-and-actions.json) | 8 | 32 | 6个W3C官方解释/实践页面 |
| [布局与密度](space-and-density.json) | 6 | 40 | CSS Grid轨道定义 |
| [为阅读设计文字](text-for-reading.json) | 8 | 40 | 10个W3C官方解释、实践和CSS规格页面 |
| [颜色与状态](color-and-state.json) | 7 | 50 | 10项W3C、Apple与Android官方技术资料的指定文字范围 |
| [深度与临时层](depth-and-layers.json) | 5 | 32 | 15项Apple、Material实现和W3C主要来源的指定文字范围 |
| [图片与用途](images-with-purpose.json) | 4 | 24 | 7项W3C与WHATWG官方技术资料的指定文字范围 |
| [收尾与真实状态](finish-and-real-states.json) | 6 | 32 | 11项IBM Carbon与W3C官方文字范围，含沿用的已读边界 |

前八篇合计49个整理页、278次图片引用观察。观察由主审读者完成，章节作者使用其记录而未独立重看原图；素材URL/哈希身份未逐一核验，次数不等于独立素材数。官方技术记录可能跨章重复，不能相加称为独立来源数；核验不替代具体产品验收。

第九篇见[指标、实验与学习效果](metrics-and-learning.json)：作者实际读取并查看本地《UX Metrics and ROI》副本的物理页101–200，保留截图微字限制；副本来源未认证，也未声称当前线上附件或全书已核。公开正文只保留原创解释、两个未实测案例和三张原创机制图；公开来源限六项登记的网页文字，原PDF、原图及私有逐页评审不随书发布。此项不并入上表的整理页/图片引用计数。

建议逐项来源记录包含：

```json
{
  "source_id": "稳定且无私人信息的编号",
  "title": "实际标题",
  "creator": null,
  "source_type": "primary_or_secondary_to_be_verified",
  "public_url": null,
  "publication_date": null,
  "version": null,
  "reviewed_scope": [],
  "claim_ids": [],
  "limitations": [],
  "reuse_basis": null
}
```

该结构是写作模板，不是某项来源已审的实例。完整规则见[PROVENANCE.md](../PROVENANCE.md)，媒体范围见[MEDIA-REVIEW.md](../MEDIA-REVIEW.md)。
