APIURLACTION = {
    'Me': {
        # 发送私信
        'SendMessage': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/messages',
            'data': {'type': 'common'},
            # receiver hash must be the user hash, not user url token
            'required_keys': ['content', 'receiver_hash']
        },
        # 设置性别
        'SetGender': {
            'method': 'put',
            'url': 'https://www.zhihu.com/api/v4/me',
            # 0 for female and 1 for male
            'required_keys': ['gender']
        },
        # 设置一句话介绍
        'SetHeadline': {
            'method': 'put',
            'url': 'https://www.zhihu.com/api/v4/me',
            'required_keys': ['headline']
        },
        # 设置居住地
        'SetLocations': {
            'method': 'put',
            'url': 'https://www.zhihu.com/api/v4/me',

            # locations should be a list of strings
            'required_keys': ['locations']
        },
        # 设置从事行业
        'SetBusiness': {
            'method': 'put',
            'url': 'https://www.zhihu.com/api/v4/me',

            # will fail silently if a wrong category is given
            'required_keys': ['business']
        },
        # 设置职业经历
        # if you want to delete certain entries, simply send the updated list (or an ampty list)
        'SetEmployments': {
            'method': 'put',
            'url': 'https://www.zhihu.com/api/v4/me',

            # employments should be a list of dictionaries {'job':'str', 'company':'str'}
            'required_keys': ['employments']
        },
        # 设置教育经历
        'SetEducations': {
            'method': 'put',
            'url': 'https://www.zhihu.com/api/v4/me',

            # employments should be a list of dictionaries {'major':'str', 'school':'str'}
            'required_keys': ['educations']
        },
        # 设置个人简介
        'SetDescription': {
            'method': 'put',
            'url': 'https://www.zhihu.com/api/v4/me',

            'required_keys': ['description']
        },
        # 提问
        'AddQuestion': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/questions',
            'data': {'type': 0},
            # is_anonymous is boolean
            'required_keys': ['title', 'topic_url_tokens', 'detail', 'is_anonymous']
        },
        # 发布想法
        'AddPin': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/pins',
            'data': {'version': '1', 'source_pin_id': '0'},
            'form_data': True,
            # content must be of form json.dumps([{'type':'text','content':'<p>xxxxxxx</p>'}])
            'required_keys': ['content']
        },
        # 创建收藏夹
        'CreateFavlist': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/favlists',
            # title and description are strings, is_public is boolean
            'required_keys': ['title', 'description', 'is_public']
        },
        # 举报
        'Report': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/reports',
            'data': {'source': 'web'},
            # type should be one of 'answer', 'question', 'pin', 'article', 'comment', 'member'
            # corresponding reason_types are listed in docs
            'required_keys': ['resource_id', 'type', 'reason_type', 'custom_reason']
        }
    },
    'Members': {
        # 关注
        'Follow': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/members/{}/followers'
        },
        # 取消关注
        'Unfollow': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/members/{}/followers'
        },
        # 屏蔽
        'Block': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/members/{}/actions/block'
        },
        # 取消屏蔽
        'Unblock': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/members/{}/actions/block'
        }
    },
    'Questions': {
        # 修改话题
        'EditTopics': {
            'method': 'put',
            'url': 'https://www.zhihu.com/api/v4/questions/{}',

            # value of question should be a dict of format {'topic_url_tokens':['topic_id1','topic_id2']}
            'required_keys': ['question']
        },
        # 修改标题
        'EditTitle': {
            'method': 'put',
            'url': 'https://www.zhihu.com/api/v4/questions/{}',

            # value of question should be a dict of format {'title':'title_of_question'}
            # value of meta should be a dict of format {'reason':'标点或格式错误'}
            'required_keys': ['question', 'meta']
        },
        # 修改补充说明
        'EditContent': {
            'method': 'put',
            'url': 'https://www.zhihu.com/api/v4/questions/{}',

            # value of question should be a dict of format {'title':'title_of_question', 'detail':'content_of_question'}
            # value of meta should be a dict of format {'reason':'标点或格式错误'}
            'required_keys': ['question', 'meta']
        },
        # 评论问题
        'AddComment': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/questions/{}/comments',

            # optional key: 'reply_to_id':comment_id
            'required_keys': ['content']
        },
        # 邀请
        'Invite': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/questions/{}/invitees',
            'data': {'src': 'search'},
            'required_keys': ['member_hash']
        },
        # 启用匿名
        'Anonymize': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/questions/{}/anonyms'
        },
        # 取消匿名
        'Deanonymize': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/questions/{}/anonyms'
        },
        # 添加回答
        'AddAnswer': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/questions/{}/answers',
            'data': {'reward_setting': {'can_reward': False}},
            'required_keys': ['content', 'reshipment_settings', 'comment_permission']
        },
        # 删除问题
        'DeleteQuestion': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/questions/{}'
        },
        # 关注问题
        'FollowQuestion': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/questions/{}/followers'
        },
        # 取消关注问题
        'UnfollowQuestion': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/questions/{}/followers'
        }
    },
    'Answers': {
        # 点赞回答
        'VoteUp': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/answers/{}/voters',
            'data': {'type': 'up'},

        },
        # 取消点赞/反对回答
        'CancelVote': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/answers/{}/voters',
            'data': {'type': 'neutral'},

        },
        # 反对回答
        'VoteDown': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/answers/{}/voters',
            'data': {'type': 'down'},

        },
        # 评论回答
        'AddComment': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/answers/{}/comments',
            # optional key: 'reply_to_id':comment_id
            'required_keys': ['content']
        },
        # 感谢回答
        'Thank': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/answers/{}/thankers'
        },
        # 取消感谢回答
        'UndoThank': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/answers/{}/thankers'
        },
        # 没有帮助
        'MarkUnhelpful': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/answers/{}/unhelpers'
        },
        # 取消没有帮助
        'UndoMarkUnhelpful': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/answers/{}/unhelpers'
        },
        # 修改评论权限
        'SetCommentPermission': {
            'method': 'put',
            'url': 'https://www.zhihu.com/api/v4/answers/{}',
            # the value should be 'all','censor','followee', or 'nobody'
            'required_keys': ['comment_permission']
        },
        # 修改转载设置
        'SetReshipmentPermission': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/answers/{}',

            # the value should be 'disallowed','allowed','need_payment'
            'required_keys': ['reshipment_settings']
        },
        # 修改回答
        'EditAnswer': {
            'method': 'put',
            'url': 'https://www.zhihu.com/api/v4/answers/{}',
            'data': {'reward_setting': {'can_reward': False}},
            'required_keys': ['content']
        },
        # 删除回答
        'DeleteAnswer': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/answers/{}'
        },
        # 撤销删除回答
        'RestoreAnswer': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/answers/{}/actions/restore'
        }
    },
    'Comments': {
        # 删除评论
        'DeleteComment': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/comments/{}'
        },
        # 点赞评论
        'LikeComment': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/comments/{}/actions/like'
        },
        # 取消点赞评论
        'UndoLikeComment': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/comments/{}/actions/like'
        },
        # 踩评论
        'DislikeComment': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/comments/{}/actions/dislike'
        },
        # 取消踩评论
        'UndoDislikeComment': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/comments/{}/actions/dislike'
        },
        # 设为推荐评论
        'Feature': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/comments/{}/actions/feature'
        },
        # 取消推荐评论
        'UndoFeature': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/comments/{}/actions/feature'
        },
        # 折叠评论
        'Collapse': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/comments/{}/actions/collapse'
        },
        # 取消折叠评论
        'UndoCollapse': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/comments/{}/actions/collapse'
        }
    },
    'Pins': {
        # 评论想法
        'AddComment': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/pins/{}/comments',
            # optional key: 'reply_to_id':comment_id
            'required_keys': ['content']
        },
        # 鼓掌想法
        'Like': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/pins/{}/reactions',
            'data': {'type': 'like'},
            'form_data': True
        },
        # 取消鼓掌想法
        'UndoLike': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/pins/{}/reactions',
            'data': {'type': 'like'}
        },
        # 删除想法
        'DeletePin': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/pins/{}'
        }
    },
    'Topics': {
        # 关注话题
        'FollowTopic': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/topics/{}/followers'
        },
        # 取消关注话题
        'UnfollowTopic': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/topics/{}/followers'
        }

    },
    'Favlists': {
        # 收藏回答/文章/想法
        'AddEntry': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/favlists/{}/items',
            # content_type should be 'answer', 'pin' or 'article'
            'required_keys': ['content_id', 'content_type']
        },
        # 评论收藏夹
        'AddComment': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/favlists/{}/comments',
            # optional key: 'reply_to_id':comment_id
            'required_keys': ['content']
        },
        # 关注收藏夹
        'FollowFavlist': {
            'method': 'post',
            'url': 'https://www.zhihu.com/collection/follow',
            'form_data': True,
            'required_keys': ['favlist_id']
        }
    },
    'Columns': {
        # 关注专栏
        'FollowColumn': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/columns/{}/followers'
        },
        # 取消关注专栏
        'UnfollowColumn': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/columns/{}/followers'
        }
    },
    'Articles': {
        # 评论文章
        'AddComment': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/articles/{}/comments',
            # optional key: 'reply_to_id':comment_id
            'required_keys': ['content']
        },
        # 修改评论权限
        'SetCommentPermission': {
            'method': 'put',
            'url': 'https://www.zhihu.com/api/v4/articles/{}',
            # the value should be 'all','censor','followee', or 'nobody'
            'required_keys': ['comment_permission']
        },
        # 删除文章
        'DeleteArticle': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/articles/{}'
        },
        # 点赞文章
        'VoteUp': {
            'method': 'post',
            'url': 'https://www.zhihu.com/api/v4/articles/{}/likers'
        },
        # 取消点赞文章
        'CancelVote': {
            'method': 'delete',
            'url': 'https://www.zhihu.com/api/v4/articles/{}/likers'
        }
    }
}
