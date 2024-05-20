<script setup lang="ts">
import { BrowseIcon, CheckCircleFilledIcon } from 'tdesign-icons-vue-next';

const img = 'https://raw.githubusercontent.com/geekmister/geekmister/master/images/cover-drawing-en.png';
</script>

<template>
  <div class="tced-page-container">
    <!-- Title area -->
    <div class="tced-page-title-area-container">
      <p class="tced-page-title-area-title">测试用例执行详情</p>
    </div>

    <!-- Summary area -->
    <div class="tced-page-summary-area-container">
      <div class="tced-page-summary-area-title-container">
        <p class="tced-page-summary-area-title">执行摘要</p>
      </div>
      <div class="tced-page-summary-area-info-container">
        <table>
          <tr>
            <td class="tced-page-summary-area-info-label-td-container tced-page-summary-area-info-td">ID</td>
            <td class="tced-page-summary-area-info-value-td-container tced-page-summary-area-info-td">1</td>
          </tr>
          <tr>
            <td class="tced-page-summary-area-info-label-td-container tced-page-summary-area-info-td">序号</td>
            <td class="tced-page-summary-area-info-value-td-container tced-page-summary-area-info-td">test-001</td>
          </tr>
          <tr>
            <td class="tced-page-summary-area-info-label-td-container tced-page-summary-area-info-td">检查点</td>
            <td class="tced-page-summary-area-info-value-td-container tced-page-summary-area-info-td">检查登录流程是否正常？</td>
          </tr>
          <tr>
            <td class="tced-page-summary-area-info-label-td-container tced-page-summary-area-info-td">前置条件</td>
            <td class="tced-page-summary-area-info-value-td-container tced-page-summary-area-info-td">打开登录页</td>
          </tr>
        </table>
        <table>
          <tr>
            <td class="tced-page-summary-area-info-label-td-container tced-page-summary-area-info-td">执行时间</td>
            <td class="tced-page-summary-area-info-value-td-container tced-page-summary-area-info-td">2024-02-05 22:43:15</td>
          </tr>
          <tr>
            <td class="tced-page-summary-area-info-label-td-container tced-page-summary-area-info-td">执行结果</td>
            <td class="tced-page-summary-area-info-value-td-container tced-page-summary-area-info-td">成功 <CheckCircleFilledIcon /></td>
          </tr>
          <tr>
            <td class="tced-page-summary-area-info-label-td-container tced-page-summary-area-info-td">日志下载</td>
            <td class="tced-page-summary-area-info-value-td-container tced-page-summary-area-info-td">点击下载</td>
          </tr>
          <tr>
            <td class="tced-page-summary-area-info-label-td-container tced-page-summary-area-info-td">步骤数量</td>
            <td class="tced-page-summary-area-info-value-td-container tced-page-summary-area-info-td">14</td>
          </tr>
        </table>
      </div>
    </div>

    <!-- Review area -->
    <div class="tced-page-review-area-container">
      <div class="tced-page-review-area-title-container">
        <p class="tced-page-review-area-title">操作回顾</p>
      </div>
      <div class="tecd-page-review-area-snapshot-container">
        <div class="tecd-page-review-area-snapshot-item-container" v-for="item in 20">
          <div class="tecd-page-review-area-snapshot-item-image-viewer-container" >
            <t-image-viewer :images="[img]">
              <template #trigger="{ open }">
                <div class="tecd-page-review-area-snapshot-item-zoom-container">
                  <img alt="test" :src="img" class="tecd-page-review-area-snapshot-item-zoom-image" />
                  <div class="tecd-page-review-area-snapshot-item-zoom-hover" @click="open">
                    <span><BrowseIcon size="1.4em" /> 预览</span>
                  </div>
                </div>
              </template>
            </t-image-viewer>
          </div>
          <span class="tecd-page-review-area-snapshot-item-name">时间{{item}}</span>
        </div>
      </div>
    </div>

    <!-- Actions area -->
    <div class="tced-page-actions-area-container">
      <div class="tced-page-actions-area-title-container">
        <p class="tced-page-actions-area-title">操作步骤</p>
      </div>
      <div class="tced-page-actions-area-details-container">
        <div class="tced-page-actions-area-details-list-container">
          <table>
            <tr>
              <td class="tced-page-actions-area-info-label-td-container">序号</td>
              <td class="tced-page-actions-area-info-label-td-container">操作</td>
              <td class="tced-page-actions-area-info-label-td-container">时长</td>
            </tr>
            <tr v-for="item in 10">
              <td class="tced-page-actions-area-info-label-td-container">#{{item}}</td>
              <td class="tced-page-actions-area-info-label-td-container">操作</td>
              <td class="tced-page-actions-area-info-label-td-container">00:00:{{item}}0</td>
            </tr>
          </table>
        </div>
        <div class="tced-page-actions-area-details-step-info-container">
          <div class="tced-page-actions-area-details-info-filter-container">
            <div class="tced-page-actions-area-details-info-filter-label">未执行</div>
            <div class="tced-page-actions-area-details-info-filter-label m-right-20">断言</div>
            <div class="tced-page-actions-area-details-info-filter-label m-right-20">失败</div>
            <div class="tced-page-actions-area-details-info-filter-label m-right-20">成功</div>
            <div class="tced-page-actions-area-details-info-filter-label m-right-20">全部</div>
            <span class="tced-page-actions-area-details-info-filter-span m-right-20">筛选:</span>
            <div class="tced-page-actions-area-details-info-filter-label m-right-100">跳转至错误步骤</div>
          </div>
          <div class="tced-page-actions-area-details-info-container">
            <p class="tecd-page-actions-area-details-step-info-content">Step 1: 点击鼠标左键操作</p>
            <p class="tecd-page-actions-area-details-step-info-content">执行结果: 成功</p>
            <p class="tecd-page-actions-area-details-step-info-content">执行时间: 2024-02-01 11:12:55</p>
            <p class="tecd-page-actions-area-details-step-info-content">执行耗时: 11:12:55</p>
            <p class="tecd-page-actions-area-details-step-info-content">执行操作: 点击鼠标左键</p>
          </div>
          <img :src="img" class="tecd-page-actions-area-details-step-info-image" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .tced-page-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    width: 100%;
  }


  .tced-page-title-area-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100px;
  }
  .tced-page-title-area-title {
    font-size: 32px;
    font-weight: bold;
    color: #FFFFFF;
    letter-spacing: 5px;
  }

  .tced-page-summary-area-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    width: calc(100% - 100px - 100px);
    height: auto;
    padding-left: 100px;
    padding-right: 100px;
    background: #121c34;
  }
  .tced-page-summary-area-title-container {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    width: 100%;
    height: 100px;
  }
  .tced-page-summary-area-title {
    font-size: 28px;
    font-weight: bold;
    color: #FFFFFF;
    letter-spacing: 5px;
  }
  .tced-page-summary-area-info-container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
    width: 100%;
    height: auto;
    padding-bottom: 50px;
  }
  .tced-page-summary-area-info-label-td-container {
    min-width: 100px;
    height: 30px;
    border: #FFFFFF;
  }
  .tced-page-summary-area-info-value-td-container {
    min-width: 200px;
    height: 30px;
    border: #FFFFFF;
  }
  .tced-page-summary-area-info-td {
    font-size: 14px;
    color: #FFFFFF;
  }

  .tced-page-review-area-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    width: calc(100% - 100px - 100px);
    height: auto;
    padding-left: 100px;
    padding-right: 100px;
    padding-bottom: 50px;
    margin-top: 100px;
    background: #121c34;
  }
  .tced-page-review-area-title-container {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    width: 100%;
    height: 100px;
  }
  .tced-page-review-area-title {
    font-size: 28px;
    font-weight: bold;
    color: #FFFFFF;
    letter-spacing: 5px;
  }
  .tecd-page-review-area-snapshot-container {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    width: 1220px;
    height: auto;
    overflow-x: scroll;
    white-space: nowrap;
  }
  .tecd-page-review-area-snapshot-item-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    width: auto;
    height: auto;
    flex-shrink: 0;
  }
  .tecd-page-review-area-snapshot-item-image-viewer-container {
    width: 160px;
    height: 160px;
    border: 4px solid #FFFFFF;
    border-radius: 4px;
  }
  .tecd-page-review-area-snapshot-item-zoom-container {
    width: 100%;
    height: 100%;
    display: inline-flex;
    position: relative;
    justify-content: center;
    align-items: center;
    border-radius: 4px;
    overflow: hidden;
  }
  .tecd-page-review-area-snapshot-item-zoom-hover {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    left: 0;
    top: 0;
    opacity: 0;
    background-color: rgba(0, 0, 0, 0.6);
    color: var(--td-text-color-anti);
    line-height: 22px;
    transition: 0.2s;
  }
  .tecd-page-review-area-snapshot-item-zoom-container:hover .tecd-page-review-area-snapshot-item-zoom-hover {
    opacity: 1;
    cursor: pointer;
  }
  .tecd-page-review-area-snapshot-item-zoom-image {
    width: auto;
    height: auto;
    max-width: 100%;
    max-height: 100%;
    cursor: pointer;
    position: absolute;
  }
  .tecd-page-review-area-snapshot-item-name {
    font-size: 14px;
    font-weight: bold;
    color: #FFFFFF;
    margin-top: 20px;
  }

  .tced-page-actions-area-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    width: calc(100% - 100px - 100px);
    height: auto;
    padding-left: 100px;
    padding-right: 100px;
    padding-bottom: 50px;
    margin-top: 100px;
    background: #121c34;
  }
  .tced-page-actions-area-title-container {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    width: 100%;
    height: 100px;
  }
  .tced-page-actions-area-title {
    font-size: 28px;
    font-weight: bold;
    color: #FFFFFF;
    letter-spacing: 5px;
  }
  .tced-page-actions-area-details-container {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    width: 100%;
    height: auto;
  }
  .tced-page-actions-area-details-list-container {
    width: auto;
    border-right: dashed #FFFFFF 1px;
  }
  .tced-page-actions-area-info-label-td-container {
    min-width: 150px;
    height: 30px;
    font-size: 14px;
    font-weight: bold;
    color: #FFFFFF;
  }
  .tced-page-actions-area-details-info-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    width: 100%;
    height: auto;
    padding-top: 20px;
    padding-bottom: 20px;
    border-bottom: dashed 1px #FFFFFF;
  }
  .tced-page-actions-area-details-info-filter-container {
    display: flex;
    flex-direction: row-reverse;
    align-items: center;
    width: 100%;
    height: 30px;
  }
  .tced-page-actions-area-details-info-filter-label {
    width: auto;
    padding-left: 10px;
    padding-right: 10px;
    font-size: 14px;
    font-weight: bold;
    color: #FFFFFF;
    background: #1F3057;
    border-radius: 5px;
  }
  .tced-page-actions-area-details-info-filter-span {
    font-weight: bold;
    color: #FFFFFF;
  }
  .tced-page-actions-area-details-step-info-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    height: auto;
    margin-left: 100px;
  }
  .tecd-page-actions-area-details-step-info-content {
    font-size: 14px;
    color: #FFFFFF;
    line-height: 40px;
  }
  .tecd-page-actions-area-details-step-info-image {
    margin-top: 30px;
    width: 100%;
  }
</style>