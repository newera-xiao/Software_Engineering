DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS rehabilitation_categories;
DROP TABLE IF EXISTS rehabilitation_knowledge;
DROP TABLE IF EXISTS medicine_feedback;
DROP TABLE IF EXISTS diagnose_feedback;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE rehabilitation_categories (
    categoryId VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO rehabilitation_categories (categoryId, name) VALUES ('category1', '膝盖疼痛'), ('category2', '肩膀损伤'), ('category3', '脊柱问题'), ('category4', '康复理论'), ('category5', '骨折康复');

CREATE TABLE rehabilitation_knowledge (
    knowledgeId VARCHAR(255) PRIMARY KEY,
    categoryId VARCHAR(255),
    title VARCHAR(255),
    content TEXT,
    image VARCHAR(255),
    video VARCHAR(255),
    source VARCHAR(255),
    timestamp TIMESTAMP,
    FOREIGN KEY (categoryId) REFERENCES rehabilitation_categories(categoryId)
);

INSERT INTO rehabilitation_knowledge (knowledgeId, categoryId, title, content, image, video, source, timestamp) VALUES
    ('knowledge1', 'category1', '常见膝盖疼痛问题及处理方法', '在康复过程中，膝盖疼痛是常见问题之一。本文介绍了膝盖疼痛的常见原因及相应的处理方法。', NULL, NULL, '医学杂志A', '2023-06-01 09:30:00'),
    ('knowledge2', 'category1', '膝盖疼痛康复运动示例', '这是一份膝盖疼痛康复运动示例，包括了针对不同类型膝盖疼痛的运动方法和注意事项。', NULL, NULL, '康复学会B', '2023-06-02 14:15:00'),
    ('knowledge3', 'category1', '膝关节保护指南', '如何保护膝关节，预防膝关节损伤？本文提供了一些建议和指南，帮助您更好地保护您的膝关节。', NULL, NULL, '健康杂志C', '2023-06-03 16:45:00'),
    ('knowledge4', 'category1', '膝关节炎的饮食建议', '膝关节炎患者在日常饮食中应该注意哪些事项？本文提供了一些膝关节炎患者的饮食建议和禁忌。', NULL, NULL, '饮食杂志D', '2023-06-04 10:10:00'),
    ('knowledge5', 'category1', '膝盖疼痛的常见治疗方法', '膝盖疼痛的治疗方法多种多样，本文总结了常见的治疗方法，帮助患者找到适合自己的治疗方案。', NULL, NULL, '医学杂志E', '2023-06-05 12:20:00'),

    ('knowledge6', 'category2', '肩膀损伤的症状和诊断', '肩膀损伤有哪些常见的症状和诊断方法？本文介绍了肩膀损伤常见的症状和诊断技术。', NULL, NULL, '医学杂志F', '2023-06-06 09:30:00'),
    ('knowledge7', 'category2', '肩膀损伤的康复训练', '针对不同类型的肩膀损伤，康复训练是非常重要的一部分。本文提供了一些肩膀损伤康复训练的示例。', NULL, NULL, '康复学会G', '2023-06-07 14:15:00'),
    ('knowledge8', 'category2', '肩袖损伤的手术治疗', '肩袖损伤需要进行手术治疗的情况较多，本文介绍了肩袖损伤手术治疗的方法和注意事项。', NULL, NULL, '外科杂志H', '2023-06-08 16:45:00'),
    ('knowledge9', 'category2', '肩膀损伤的康复护理', '肩膀损伤患者在康复过程中需要注意哪些护理事项？本文提供了一些建议和指导。', NULL, NULL, '护理杂志I', '2023-06-09 10:10:00'),
    ('knowledge10', 'category2', '肩膀损伤的康复辅助器具', '在肩膀损伤康复过程中，一些辅助器具可以起到帮助和支持的作用。本文介绍了常见的康复辅助器具。', NULL, NULL, '康复学报J', '2023-06-10 12:20:00');

-- Category 3: 脊柱问题
INSERT INTO rehabilitation_knowledge (knowledgeId, categoryId, title, content, image, video, source, timestamp) VALUES
    ('knowledge11', 'category3', '脊柱问题的常见症状和治疗', '脊柱问题可能导致背部疼痛和其他症状。本文介绍了常见的脊柱问题症状和治疗方法。', NULL, NULL, '医学杂志K', '2023-06-11 09:30:00'),
    ('knowledge12', 'category3', '脊柱问题的物理疗法', '物理疗法在脊柱问题的康复中起到重要作用。本文介绍了常见的脊柱问题物理疗法方法和注意事项。', NULL, NULL, '康复学会L', '2023-06-12 14:15:00'),
    ('knowledge13', 'category3', '脊柱问题的手术治疗', '一些严重的脊柱问题可能需要进行手术治疗。本文介绍了脊柱问题手术治疗的方法和风险。', NULL, NULL, '外科杂志M', '2023-06-13 16:45:00'),
    ('knowledge14', 'category3', '脊柱问题的康复体操', '脊柱问题的康复体操可以帮助增强脊柱肌肉和改善姿势。本文提供了一些脊柱问题康复体操示例。', NULL, NULL, '康复学报N', '2023-06-14 10:10:00'),
    ('knowledge15', 'category3', '预防脊柱问题的方法', '如何预防脊柱问题的发生？本文提供了一些预防脊柱问题的方法和建议。', NULL, NULL, '健康杂志O', '2023-06-15 12:20:00');

-- Category 4: 康复理论
INSERT INTO rehabilitation_knowledge (knowledgeId, categoryId, title, content, image, video, source, timestamp) VALUES
    ('knowledge16', 'category4', '康复理论概述', '康复理论是康复医学的基础，本文对康复理论的基本概念和原则进行了介绍。', NULL, NULL, '医学杂志P', '2023-06-16 09:30:00'),
    ('knowledge17', 'category4', '康复评估与测量', '康复评估和测量是确定患者康复进程和效果的重要手段。本文介绍了常用的康复评估和测量方法。', NULL, NULL, '康复学会Q', '2023-06-17 14:15:00'),
    ('knowledge18', 'category4', '康复计划制定与执行', '康复计划的制定和执行是康复治疗的核心步骤。本文介绍了康复计划的制定和执行策略。', NULL, NULL, '康复学报R', '2023-06-18 16:45:00'),
    ('knowledge19', 'category4', '康复研究与进展', '康复研究不断推动康复医学的发展。本文概述了近期康复研究的一些重要进展和成果。', NULL, NULL, '医学杂志S', '2023-06-19 10:10:00'),
    ('knowledge20', 'category4', '康复专家的角色与责任', '康复专家在康复治疗中起着重要的角色。本文探讨了康复专家的角色与责任。', NULL, NULL, '康复学会T', '2023-06-20 12:20:00');

-- Category 5: 骨折康复
INSERT INTO rehabilitation_knowledge (knowledgeId, categoryId, title, content, image, video, source, timestamp) VALUES
    ('knowledge21', 'category5', '骨折康复的基本原则', '骨折康复的基本原则是保护骨折部位并促进骨折愈合。本文介绍了骨折康复的基本原则和注意事项。', NULL, NULL, '医学杂志U', '2023-06-21 09:30:00'),
    ('knowledge22', 'category5', '骨折康复的康复训练', '骨折康复训练有助于恢复骨折部位的功能和力量。本文提供了一些骨折康复训练的示例和指导。', NULL, NULL, '康复学会V', '2023-06-22 14:15:00'),
    ('knowledge23', 'category5', '骨折康复的日常护理', '骨折康复期间需要注意一些日常护理事项，以促进骨折愈合。本文提供了一些建议和指导。', NULL, NULL, '护理杂志W', '2023-06-23 16:45:00'),
    ('knowledge24', 'category5', '骨折康复的营养建议', '合理的营养摄入对于骨折康复至关重要。本文介绍了骨折康复期间的营养建议和饮食指导。', NULL, NULL, '营养学刊X', '2023-06-24 10:10:00'),
    ('knowledge25', 'category5', '骨折康复的心理支持', '骨折康复期间的心理支持对于患者的康复非常重要。本文提供了一些心理支持的方法和建议。', NULL, NULL, '心理学杂志Y', '2023-06-25 12:20:00');

CREATE TABLE medicine_feedback (
    feecbackId INTEGER PRIMARY KEY AUTOINCREMENT,
    patientId INTEGER,
    medicineID INTEGER,
    feedbackContent TEXT,
    feedbackDate TEXT,
    FOREIGN KEY(patientId) REFERENCES user(id)
);

CREATE TABLE diagnose_feedback (
    feecbackId INTEGER PRIMARY KEY AUTOINCREMENT,
    patientId INTEGER,
    doctor INTEGER,
    feedbackContent TEXT,
    feedbackDate TEXT,
    FOREIGN KEY(patientId) REFERENCES user(id)
);
