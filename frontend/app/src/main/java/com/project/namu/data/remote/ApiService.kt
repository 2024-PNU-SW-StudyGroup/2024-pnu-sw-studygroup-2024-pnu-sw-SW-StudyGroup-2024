package com.project.namu.data.remote
import com.project.namu.data.model.StoreData
import retrofit2.Response
import retrofit2.http.GET



interface ApiService {
    @GET("store/list")
    // 최상위가 배열이므로, Response<List<StoreData>>로 선언
    suspend fun getStoreList(): Response<List<StoreData>>


}