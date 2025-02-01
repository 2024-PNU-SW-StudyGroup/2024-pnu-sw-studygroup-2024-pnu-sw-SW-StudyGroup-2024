package com.project.namu.ui.page

import android.util.Log
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Favorite
import androidx.compose.material.icons.filled.FavoriteBorder
import androidx.compose.material.icons.filled.Star
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.Icon
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
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
import com.project.namu.ui.tools.PagerWithDotsIndicator
import com.project.namu.ui.theme.BackGround
import com.project.namu.R
import com.project.namu.data.model.SetInfo
import com.project.namu.data.model.StoreDetailData
import com.project.namu.ui.component.Store_SwitchBottomBar
import com.project.namu.ui.viewmodel.StoreDetailUiState
import com.project.namu.ui.viewmodel.StoreDetailViewModel


@Composable
fun StoreScreen(
    navController: NavController,
    storeId: Int,  // ← NavController로부터 넘겨받을 storeId
    viewModel: StoreDetailViewModel = androidx.lifecycle.viewmodel.compose.viewModel()
) {
    Log.d("DEBUG", "StoreScreen started with storeId=$storeId")

    // 1) ViewModel이 들고 있는 uiState
    val uiState by viewModel.uiState.collectAsState()

    // 2) 화면이 처음 만들어질 때(또는 storeId 바뀔 때) 서버 호출
    LaunchedEffect(storeId) {
        // 5번 체크: storeId가 0이면 서버 요청을 보낼지 말지 분기할 수도 있음
        if (storeId == 0) {
            Log.e("DEBUG", "Warning: storeId is 0 — check your data.")
        } else {
            viewModel.getStoreDetail(storeId)
        }
    }

    // 3) uiState 상태에 따라 분기처리
    Scaffold(
        topBar = { /*...*/ },
        bottomBar = {
            Store_SwitchBottomBar(isAvailable = true)
        },
    ) { paddingValues ->
        Box(modifier = Modifier.padding(paddingValues)) {
            when (uiState) {
                is StoreDetailUiState.Loading -> {
                    Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                        CircularProgressIndicator()
                    }
                }
                is StoreDetailUiState.Success -> {
                    val storeDetailData = (uiState as StoreDetailUiState.Success).data
                    StoreContent(storeDetailData)
                }
                is StoreDetailUiState.Error -> {
                    val message = (uiState as StoreDetailUiState.Error).message
                    Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                        Text(text = "에러: $message", color = Color.Red)
                    }
                }
            }

        }
    }
}


@Composable
fun StoreContent(storeDetailData: StoreDetailData) {
    LazyColumn(
        modifier = Modifier
            .fillMaxSize()
            .background(color = BackGround)
    ) {
        // 1) 사진/이미지 Pager
        item {
            Store_Pager(imageUrl = storeDetailData.storePictureUrl)
        }

        // 2) 가게 기본 정보 표시
        item {
            Store_Detail(
                storeName = storeDetailData.storeName,
                storePhone = storeDetailData.storePhone,
                pickupTimes = storeDetailData.pickupTimes,
                storeAddress = storeDetailData.storeAddress,
                storeRating = storeDetailData.storeRating,
                reviewCount = storeDetailData.reviewCount
            )
        }

        // 3) 메뉴 목록
        items(storeDetailData.setNames.size) { index ->
            val menuItem = storeDetailData.setNames[index]
            Store_MenuDetail(
                menuData = menuItem
            )
        }
    }
}


@Composable
fun Store_Pager(imageUrl: String) {
    var isFavorite by remember { mutableStateOf(false) }

    Box {
        // 이미지 슬라이더/페이저
        // 여기서 imageUrl을 coil/glide 등으로 로드할 수도 있음
        PagerWithDotsIndicator(
            indicatorColor = Color.White,
            pageCount = 1, // 일단 1장만 있다고 가정
            pageContent = { page ->
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(230.dp)
                ) {
                    // 예시) Coil로 이미지 로드
                    // Image(painter = rememberAsyncImagePainter(imageUrl), contentDescription = "가게 사진")
                }
            }
        )

        // 오른쪽 상단 아이콘(장바구니, 좋아요)
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

//페이저 아래 가게 이름 ~ 설명
@Composable
fun Store_Detail(
    storeName: String,
    storePhone: String,
    pickupTimes: String,
    storeAddress: String,
    storeRating: Float,
    reviewCount: Int
) {
    Box(
        modifier = Modifier
            .fillMaxWidth()
            .height(170.dp)
            .background(Color.White)
    ) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(20.dp)
        ) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = storeName, // 동적 데이터
                    fontSize = 24.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color.Black
                )

                Spacer(modifier = Modifier.width(80.dp))

                // 별점 표시
                Row {
                    Icon(
                        imageVector = Icons.Default.Star,
                        contentDescription = "Rating",
                        tint = Color(0xFFFFD607),
                        modifier = Modifier.size(24.dp)
                    )
                    Spacer(modifier = Modifier.width(4.dp))
                    Text(
                        text = storeRating.toString(), // 동적 데이터
                        fontSize = 18.sp,
                        color = Color.Black,
                        fontWeight = FontWeight.Medium
                    )
                }
            }

            Spacer(modifier = Modifier.height(20.dp))

            // 가게 전화번호
            Row(verticalAlignment = Alignment.CenterVertically) {
                Image(
                    painter = painterResource(id = R.drawable.card_clock),
                    contentDescription = "phonenumber",
                    modifier = Modifier.size(18.dp)
                )
                Spacer(modifier = Modifier.width(8.dp))
                Text(
                    text = storePhone, // 동적 데이터
                    fontSize = 16.sp,
                    color = Color.Black,
                    fontWeight = FontWeight.Normal,
                )
            }

            // 영업시간
            // ...
            // 위치
            // ...
        }

        // 리뷰 N개 버튼
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(180.dp)
                .padding(20.dp),
            contentAlignment = Alignment.BottomEnd
        ) {
            Button(
                onClick = { /* TODO */ },
                modifier = Modifier
                    .border(
                        width = 1.dp,
                        color = Color(0xFFE7E7E7),
                        shape = RoundedCornerShape(size = 30.dp)
                    )
                    .width(100.dp)
                    .height(32.dp),
                colors = ButtonDefaults.buttonColors(
                    containerColor = Color.Transparent,
                    contentColor = Color.Black
                )
            ) {
                Text(text = "리뷰 ${reviewCount}+개") // 동적 리뷰 수
            }
        }
    }
}

@Composable
fun Store_MenuDetail(menuData: SetInfo) {
    Card(
        shape = RoundedCornerShape(16.dp),
        colors = CardDefaults.cardColors(containerColor = Color.White),
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 20.dp)
            .padding(top = 10.dp)
            .height(165.dp)
    ) {
        Row(
            modifier = Modifier.fillMaxSize()
        ) {
            // 왼쪽 이미지
            Box(
                modifier = Modifier
                    .width(120.dp)
                    .fillMaxHeight()
            ) {
                // 예) Coil로 메뉴 이미지 로드
                // Image(
                //     painter = rememberAsyncImagePainter(menuData.menuPictureUrl),
                //     contentDescription = null,
                //     modifier = Modifier.fillMaxSize()
                // )
            }

            // 오른쪽 텍스트
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(12.dp)
            ) {
                Text(
                    text = menuData.setName,  // 동적 데이터
                    fontSize = 20.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color.Black
                )
                Spacer(modifier = Modifier.height(4.dp))

                Text(
                    text = menuData.menuNames,
                    fontSize = 16.sp,
                    color = Color.Black
                )
                Spacer(modifier = Modifier.height(4.dp))

                Text(
                    text = menuData.menuDetail,
                    fontSize = 12.sp,
                    fontWeight = FontWeight.Medium,
                    color = Color(0xFF8B8B8B),
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )
                Spacer(modifier = Modifier.height(10.dp))

                // 할인율 계산(예: 원래 가격 - 할인 가격)
                val discountPercent = ((menuData.menuPrice - menuData.menuDiscountPrice).toFloat() / menuData.menuPrice * 100).toInt()

                Row(verticalAlignment = Alignment.CenterVertically) {
                    Text(
                        text = "${discountPercent}%",
                        fontSize = 16.sp,
                        fontWeight = FontWeight.Bold,
                        color = Color(0xFF4CAF50)
                    )
                    Spacer(modifier = Modifier.width(8.dp))

                    Text(
                        text = "${menuData.menuDiscountPrice}원",
                        fontSize = 16.sp,
                        fontWeight = FontWeight.Bold,
                        color = Color.Black
                    )
                    Spacer(modifier = Modifier.width(8.dp))

                    Text(
                        text = "${menuData.menuPrice}원",
                        fontSize = 14.sp,
                        color = Color(0xFF8B8B8B),
                        textDecoration = TextDecoration.LineThrough
                    )
                }
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun StorePreview() {
    val navController = rememberNavController()

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(Color.White) // 전체 배경색 설정
    ) {
    }
}

