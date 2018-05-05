APIURLGET = {
    'Me': {
        # 账号信息
        'Info': 'https://www.zhihu.com/api/v4/me',
        # 私信
        'Messages': 'https://www.zhihu.com/api/v4/me/message-threads',
        # 通知
        'Notifications': 'https://www.zhihu.com/api/v4/notifications/v2/default'
    },
    'Members': {
        # 用户信息
        'Info': 'https://www.zhihu.com/api/v4/members/{}',
        # 关注的人
        'Followees': 'https://www.zhihu.com/api/v4/members/{}/followees',
        # 关注者
        'Followers': 'https://www.zhihu.com/api/v4/members/{}/followers',
        # 关注的问题
        'FollowingQuestions': 'https://www.zhihu.com/api/v4/members/{}/following-questions',
        # 关注的话题
        'FollowingTopics': 'https://www.zhihu.com/api/v4/members/{}/following-topic-contributions',
        # 关注的专栏
        'FollowingColumns': 'https://www.zhihu.com/api/v4/members/{}/following-columns',
        # 关注的收藏夹
        'FollowingFavlists': 'https://www.zhihu.com/api/v4/members/{}/following-favlists',
        # 提问
        'Questions': 'https://www.zhihu.com/api/v4/members/{}/questions',
        # 回答
        'Answers': 'https://www.zhihu.com/api/v4/members/{}/answers',
        # 想法
        'Pins': 'https://www.zhihu.com/api/v4/members/{}/pins',
        # 文章
        'Articles': 'https://www.zhihu.com/api/v4/members/{}/articles',
        # 专栏
        'Columns': 'https://www.zhihu.com/api/v4/members/{}/column-contributions',
        # 收藏
        'Favlists': 'https://www.zhihu.com/api/v4/members/{}/favlists',
        # 动态
        'Activities': 'https://www.zhihu.com/api/v4/members/{}/activities'
    },
    'Questions': {
        # 问题信息
        'Info': 'https://www.zhihu.com/api/v4/questions/{}',
        # 关注者
        'Followers': 'https://www.zhihu.com/api/v4/questions/{}/concerned_followers',
        # 评论
        'Comments': 'https://www.zhihu.com/api/v4/questions/{}/comments',
        # 被邀请的人
        'Invitees': 'https://www.zhihu.com/api/v4/questions/{}/invitees',
        # 可能被邀请的人
        'InvitationCandidates': 'https://www.zhihu.com/api/v4/questions/{}/invitation-candidates',
        # 相关问题
        'SimilarQuestions': 'https://www.zhihu.com/api/v4/questions/{}/similar-questions',
        #
        'MetaRelatedTopics': 'https://www.zhihu.com/api/v4/questions/{}/meta_related_topics',
        # 相关推荐
        'RelatedKnowledgeCommodities': 'https://www.zhihu.com/api/v4/questions/{}/related-knowledge-commodities'

    },
    'Answers': {
        # 回答信息
        'Info': 'https://www.zhihu.com/api/v4/answers/{}',
        # 点赞者
        'Upvoters': 'https://www.zhihu.com/api/v4/answers/{}/concerned_upvoters',
        # 评论
        'Comments': 'https://www.zhihu.com/api/v4/answers/{}/comments'
    },
    'Comments': {
        # 评论信息
        'Info': 'https://www.zhihu.com/api/v4/comments/{}',
        # 包含某评论的对话
        'CommentsWithConversation': 'https://www.zhihu.com/api/v4/comments/{}/conversation'
    },
    'Pins': {
        # 想法信息
        'Info': 'https://www.zhihu.com/api/v4/pins/{}',
        # 评论
        'Comments': 'https://www.zhihu.com/api/v4/pins/{}/comments'
    },
    'Favlists': {
        # 收藏夹信息
        'Info': 'https://www.zhihu.com/api/v4/favlists/{}',
        # 收藏夹内容
        'Items': 'http://www.zhihu.com/api/v4/favlists/{}/items',
        # 收藏夹评论
        'Comments': 'http://www.zhihu.com/api/v4/favlists/{}/comments',
        # 收藏夹关注者
        'Followers': 'http://www.zhihu.com/api/v4/favlists/{}/followers'
    },
    'Topics': {
        # 话题信息
        'Info': 'https://www.zhihu.com/api/v4/topics/{}',
        # 关注者
        'Followers': 'https://www.zhihu.com/api/v4/topics/{}/followers',
        # 精华
        'Essence': 'https://www.zhihu.com/api/v4/topics/{}/feeds/essence',
        # 精华问题
        'TopQuestions': 'https://www.zhihu.com/api/v4/topics/{}/feeds/top_question',
        # 最新问题
        'TimelineQuestions': 'https://www.zhihu.com/api/v4/topics/{}/feeds/timeline_question',
        # 优秀答主
        'BestAnswerers': 'https://www.zhihu.com/api/v4/topics/{}/best_answerers',
        # 精华动态
        'TopActivities': 'https://www.zhihu.com/api/v4/topics/{}/feeds/top_activity',
        # 最新动态
        'TimelineActivities': 'https://www.zhihu.com/api/v4/topics/{}/feeds/timeline_activity'
    },
    'Articles': {
        # 文章信息
        'Info': 'https://zhuanlan.zhihu.com/api/posts/{}',
        # 点赞者
        'Upvoters': 'https://zhuanlan.zhihu.com/api/posts/{}/likers',
        # 文章评论
        'Comments': 'https://zhuanlan.zhihu.com/api/posts/{}/comments'
    },
    'Columns': {
        # 专栏信息
        'Info': 'https://zhuanlan.zhihu.com/api/columns/{}',
        # 关注者
        'Followers': 'https://zhuanlan.zhihu.com/api/columns/{}/followers',
        # 文章
        'Posts': 'https://zhuanlan.zhihu.com/api/columns/{}/posts'
    }

}
