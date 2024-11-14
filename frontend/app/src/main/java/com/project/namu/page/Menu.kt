package com.project.namu.page

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Favorite
import androidx.compose.material.icons.filled.FavoriteBorder
import androidx.compose.material3.Icon
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import androidx.navigation.compose.rememberNavController
import com.project.namu.R
import com.project.namu.component.Menu_BottomBar
import com.project.namu.component.Store_SwitchBottomBar
import com.project.namu.tools.PagerWithDotsIndicator
import com.project.namu.ui.theme.Ui_empty


@Composable
fun MenuScreen(navController: NavController) {
    var selectedIndex by remember { mutableStateOf(0) }

    Scaffold(
        topBar = { },

        bottomBar = {
            Menu_BottomBar()
        },

        content = { paddingValues ->
            Box(modifier = Modifier.padding(paddingValues)) {
                // 메인 콘텐츠
                MenuContent()
            }
        }
    )
}

@Composable
fun MenuContent() {
    Column(
    ) {
        Menu_Image()

        Row(
            modifier = Modifier
                .padding(20.dp)
                .fillMaxWidth(),
            verticalAlignment = Alignment.CenterVertically,
            ){
            Text(
                text = "세트 A",
                fontSize = 24.sp,
                fontWeight = FontWeight.Bold,
                color = Color.Black
            )

            // 메뉴 구성
            Text(
                text = "애플 와플 (1), 콘치폭 핫도그 (1)",
                fontSize = 20.sp,
                color = Color.Black
            )
        }


        Spacer(modifier = Modifier.height(4.dp))

        // 메뉴 설명
        Text(
            text = "어린시절 즐겨먹던 달콤한 사과쨈에 수제 생크림을 듬뿍 넣은 바삭한 와플과 소시지의 육즙이 팡팡 터지는 핫도그에 다양한 토핑이 듬뿍 들어간 핫도그",
            fontSize = 12.sp,
            fontWeight = FontWeight.Medium,
            color = Color(0xFF8B8B8B),
        )

        Spacer(modifier = Modifier.height(10.dp))

        // 할인 정보 및 가격
        Row(
            verticalAlignment = Alignment.CenterVertically
        ) {
            // 할인율
            Text(
                text = "30%",
                fontSize = 16.sp,
                fontWeight = FontWeight.Bold,
                color = Color(0xFF4CAF50) // Green color for discount
            )

            Spacer(modifier = Modifier.width(8.dp))

            // 할인된 가격
            Text(
                text = "7,070원",
                fontSize = 16.sp,
                fontWeight = FontWeight.Bold,
                color = Color.Black
            )

            Spacer(modifier = Modifier.width(8.dp))

            // 원래 가격 (취소선)
            Text(
                text = "10,100원",
                fontSize = 14.sp,
                color = Color(0xFF8B8B8B),
                textDecoration = TextDecoration.LineThrough
            )
        }
    }

}


@Composable
fun Menu_Image() {
    var isFavorite by remember { mutableStateOf(false) } // 좋아요 상태

    Box {


        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(230.dp)
                .background(color = Ui_empty)
        ) {

        }


        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(230.dp)
        ) {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(18.dp),
                horizontalArrangement = Arrangement.End
            ) {
                Icon(
                    painter = painterResource(id = R.drawable.ic_shopping),
                    contentDescription = "장바구니",
                    tint = Color.White,
                    modifier = Modifier
                        .padding(8.dp)
                        .size(28.dp)
                )
                Icon(
                    imageVector = if (isFavorite) Icons.Default.Favorite else Icons.Default.FavoriteBorder,
                    contentDescription = "Like",
                    tint = Color.White,
                    modifier = Modifier
                        .padding(8.dp)
                        .clickable { isFavorite = !isFavorite }
                        .size(28.dp)
                )
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun MenuPreview() {
    val navController = rememberNavController()

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(Color.White) // 전체 배경색 설정
    ) {
        MenuScreen(navController = navController)
    }
}

