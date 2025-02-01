package com.project.namu.data.model

import com.google.gson.annotations.SerializedName

data class StoreData(
    @SerializedName("storeId") val storeId: Int,
    @SerializedName("storeName") val storeName: String,
    @SerializedName("storeCategory") val storeCategory: String,
    @SerializedName("pickupTimes") val pickupTimes: String,
    @SerializedName("minPrice") val minPrice: Int,
    @SerializedName("reviewCount") val reviewCount: Int,
    @SerializedName("orderCount") val orderCount: Int,
    @SerializedName("storeRating") val storeRating: Float,
    @SerializedName("location") val location: Int,

    @SerializedName("open") val open: Boolean,
    @SerializedName("setNames") val setNames: List<SetInfo>
)

data class SetInfo(
    @SerializedName("setName") val setName: String,
    @SerializedName("menuNames") val menuNames: String = ""
)

