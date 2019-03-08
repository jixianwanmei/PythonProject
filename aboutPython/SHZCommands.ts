const { ccclass, property } = cc._decorator;

@ccclass
export default class SHZCommands {


/**-----------------------------------------------------------------------------*/
   
/** 服务定义*/


public static KIND_ID : number = 203;

public static GAME_PLAYER : number = 1;


/** 简单的版本检测*/

/** 如果客户端有更新应该更改这个值. 如果只修改EXE的版本而网络数据包没修改的话,*/

/** 更新客户端是没什么意义的, 因为EXE的版本是可以直接被修改的, 只要保存以前的*/

/** EXE版本, 更新完之后再换回去, 如果有BUG的话等于还是没修复.*/







/**-----------------------------------------------------------------------------*/

/** 游戏定义*/


/** 游戏图标*/




public static MAX_ITEMS : number = 50;

/**struct tagMStock*/

/**{*/

/**	WORD  wStyle;*/

/**	WORD  wServerID;*/

/**	SCORE lscore;*/

/**	TCHAR szTitleinfo[128];*/

/**};*/














public static  kMaxRecordsCount:number = 15;

/**-----------------------------------------------------------------------------*/

/** 服务端命令*/

/** 滚动结果*/
public static SUB_S_SCENE1_START : number = 100;             
/** 骰子结果*/
public static SUB_S_SCENE2_RESULT : number = 101;             
/** 玛丽结果*/
public static SUB_S_SCENE3_RESULT : number = 102;             
/** 库存操作结果*/
public static SUB_S_STOCK_RESULT : number = 103;             
/** 概率查询结果*/
public static SUB_S_PRO_INQUIRY_RESULT : number = 104;             
/** 个人结果*/
public static SUB_S_PERSON_RESULT : number = 105;             
/** 比倍记录*/
public static SUB_S_DOUBLE_RECORD : number = 106;             
/** 上分成功*/
public static SUB_S_ADD_CREDIT_SCORE_SUCCESS : number = 107;				
/** 上分失败*/
public static SUB_S_ADD_CREDIT_SCORE_FAILS : number = 108;				
/** 下分*/
public static SUB_S_SCORE : number = 109;				
/** 用户下注*/
public static SUB_S_USERBET : number = 110;				
/** 游戏场景*/
public static SUB_S_SCENE : number = 111;				
/** 全盘奖励*/
public static SUB_S_OVERALL_REWARD : number = 112;				

/** 救济金成功*/
public static SUB_S_TAKE_GOLD_SUCCESS : number = 113;				
/** 救济金失败*/
public static SUB_S_TAKE_GOLD_FAILURE : number = 114;				
/** 在线奖励*/
public static SUB_S_TAKE_ONLINE_REWARD : number = 115;				
/** 在线奖励配置结果*/
public static SUB_S_RESULT_ONLINE_REWARD_CONFIG : number = 116;				
/** 奖励剩余时间*/
public static SUB_S_RESULT_ONLINE_REWARD_TIME : number = 117;				
/** 重置在线奖励*/
public static SUB_S_RESET_ONLINE_REWARD : number = 118;				

























/**-----------------------------------------------------------------------------*/

/** 客户端命令*/


/** 上分*/
public static SUB_C_ADD_CREDIT_SCORE : number = 1;               
/** 下分*/
public static SUB_C_REDUCE_CREDIT_SCORE : number = 2;               
/***/
public static SUB_C_SCENE1_START : number = 3;               
/** 买大小*/
public static SUB_C_SCENE2_BUY_TYPE : number = 4;               
/** 得分*/
public static SUB_C_SCORE : number = 5;               
/***/
public static SUB_C_SCENE3_START : number = 6;               


public static SUB_C_GLOBAL_MESSAGE : number = 7;
public static SUB_C_STOCK_OPERATE : number = 8;
/** 概率查询*/
public static SUB_C_PRO_INQUIRY : number = 9;               
/** 保存概率*/
public static SUB_C_SAVE_PRO : number = 10;              
/** 个人控制*/
public static SUB_C_PERSON_CONTROL : number = 11;              
/** 起立*/
public static SUC_C_STAND_UP : number = 12;				
/** 领取救济金*/
public static SUB_C_GET_TAKE_GOLD : number = 13;				
/** 领取在线奖励*/
public static SUB_C_GET_ONLINE_REWARD : number = 14;				
/** 查询剩余时间*/
public static SUB_C_QUERY_ONLINE_REWARD_TIME : number = 15;				
/** 查询在线奖励配置*/
public static SUB_C_QUERY_ONLINE_REWARD_CONFIG : number = 16;				
































}