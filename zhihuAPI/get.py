APIURLGET = {
    "Miscellaneous": {
        # 账号信息
        "Me": "https://www.zhihu.com/api/v4/me",
        # 用户信息
        "Profile": "https://www.zhihu.com/api/v4/members/{}",
        # 话题信息
        "Topic": "https://www.zhihu.com/api/v4/topics/{}",
        # 问题信息
        "Question": "https://www.zhihu.com/api/v4/questions/{}",
        # 私信
        "Messages": "https://www.zhihu.com/api/v4/messages",
        # 通知
        "Notifications": "https://www.zhihu.com/api/v4/default-notifications"
    },
    "Members": {
        # 关注的人
        "Followees": "https://www.zhihu.com/api/v4/members/{}/followees",
        # 关注者
        "Followers": "https://www.zhihu.com/api/v4/members/{}/followers",
        # 关注的问题
        "FollowingQuestions": "https://www.zhihu.com/api/v4/members/{}/following-questions",
        # 关注的话题
        "FollowingTopics": "https://www.zhihu.com/api/v4/members/{}/following-topic-contributions",
        # 关注的专栏
        "FollowingColumns": "https://www.zhihu.com/api/v4/members/{}/following-columns",
        # 关注的收藏夹
        "FollowingFavlists": "https://www.zhihu.com/api/v4/members/{}/following-favlists",
        # 提问
        "Questions": "https://www.zhihu.com/api/v4/members/{}/questions",
        # 回答
        "Answers": "https://www.zhihu.com/api/v4/members/{}/answers",
        # 想法
        "Pins": "https://www.zhihu.com/api/v4/members/{}/pins",
        # 文章
        "Articles": "https://www.zhihu.com/api/v4/members/{}/articles",
        # 专栏
        "Columns": "https://www.zhihu.com/api/v4/members/{}/column-contributions",
        # 收藏
        "Favlists": "https://www.zhihu.com/api/v4/members/{}/favlists",
        # 动态
        "Activities": "https://www.zhihu.com/api/v4/members/{}/activities"
    },
    "Questions": {
        # 关注者
        "Followers": "https://www.zhihu.com/api/v4/questions/{}/concerned_followers",
        # 评论
        "Comments": "https://www.zhihu.com/api/v4/questions/{}/comments",
        # 被邀请的人
        "Invitees": "https://www.zhihu.com/api/v4/questions/{}/invitees",
        # 可能被邀请的人
        "InvitationCandidates": "https://www.zhihu.com/api/v4/questions/{}/invitation-candidates"
    },
    "Answers": {
        # 点赞者
        "Upvoters": "https://www.zhihu.com/api/v4/answers/{}/concerned_upvoters",
        # 评论
        "Comments": "https://www.zhihu.com/api/v4/answers/{}/comments"
    },
    "Pins": {
        # 评论
        "Comments": "https://www.zhihu.com/api/v4/pins/{}/comments"
    },
    "Topics": {
        # 关注者
        "Followers": "https://www.zhihu.com/api/v4/topics/{}/followers",
        # 精华
        "Essence": "https://www.zhihu.com/api/v4/topics/{}/feeds/essence",
        # 精华问题
        "TopQuestions": "https://www.zhihu.com/api/v4/topics/{}/feeds/top_question",
        # 最新问题
        "TimelineQuestions": "https://www.zhihu.com/api/v4/topics/{}/feeds/timeline_question",
        # 优秀答主
        "BestAnswerers": "https://www.zhihu.com/api/v4/topics/{}/best_answerers",
        # 精华动态
        "TopActivities": "https://www.zhihu.com/api/v4/topics/{}/feeds/top_activity",
        # 最新动态
        "TimelineActivities": "https://www.zhihu.com/api/v4/topics/{}/feeds/timeline_activity"
    },
    "Articles": {
        # 点赞者
        "Upvoters": "https://zhuanlan.zhihu.com/api/posts/{}/likers",
        # 文章评论
        "Comments": "https://zhuanlan.zhihu.com/api/posts/{}/comments"
    },
    "Columns": {
        # 关注者
        "Followers": "https://zhuanlan.zhihu.com/api/columns/{}/followers",
        # 文章
        "Posts": "https://zhuanlan.zhihu.com/api/columns/{}/posts"
    }

}
